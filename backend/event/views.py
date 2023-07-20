from django.http import HttpResponse
import requests
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_lib import SSLCOMMERZ
import requests
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import redirect



class EventView(ListAPIView):
    permission_classes = AllowAny,
    pagination_class = PageNumberPagination
    serializer_class = EventSerializer
    ordering = ['-event_date_start',]

    def get_queryset(self):
        limit = self.request.query_params.get('limit')
        if limit:
            return Event.objects.all()[:int(limit)]
        return Event.objects.exclude(is_active=False)


class EventDetailView(RetrieveAPIView):
    permission_classes = AllowAny,
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer


@csrf_exempt
def EventPayment(request):
    sslcz = SSLCOMMERZ({'store_id': 'bhtpa5f97c55758c00',
                       'store_pass': 'bhtpa5f97c55758c00@ssl', 'issandbox': True})
    
    data = {
        'total_amount': "100.26",
        'currency': "BDT",
        'tran_id': "tran_12345",
        'success_url': "http://127.0.0.1:3000/payment-successful", # if transaction is succesful, user will be redirected here
        'fail_url': "http://127.0.0.1:3000/payment-failed", # if transaction is failed, user will be redirected here
        'cancel_url': "http://127.0.0.1:3000/payment-cancelled", # after user cancels the transaction, will be redirected here
        'emi_option': "0",
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general",
    }
    response = sslcz.createSession(data)
    return redirect(response['GatewayPageURL'])