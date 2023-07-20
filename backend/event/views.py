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
    
    post_body = {}
    post_body['total_amount'] = 100.26
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "your success url"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    return HttpResponse(response)