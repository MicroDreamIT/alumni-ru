from django.contrib.auth.models import User
from django.db import models
from rest_framework.exceptions import ValidationError
from .enums import Gender


class Profile(models.Model):
    def validate_image(self):
        file_size = self.file.size
        megabyte_limit = 5.0
        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, db_index=True, null=False)
    gender = models.CharField(default='M', max_length=1, choices=[(choice.value, choice.name) for choice in Gender])
    avatar = models.ImageField(default='default.png', upload_to='profile_pics', validators=[validate_image])
    subject = models.CharField(max_length=100, db_index=True)
    batch_no = models.CharField(max_length=100, db_index=True)
    enroll_year = models.CharField(max_length=4, db_index=True)
    graduation_year = models.CharField(max_length=4, db_index=True)
    street_address = models.CharField(max_length=191)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    paid_amount = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
