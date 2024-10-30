from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

    
class Customer(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_country = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_address_line_1 = models.CharField(max_length=255)  
    user_address_line_2 = models.CharField(max_length=255) 
    user_pin_code = models.BigIntegerField()
    user_state = models.CharField(max_length=50)  
    user_profile_photo = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50,default='customer')
    user_old_password = models.CharField(max_length=128, blank=True, null=True)
    user_joined_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now,blank=True,null=True)
    users_daily_limit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )
    users_monthly_limit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )
    class Meta:
        db_table = 'users'
        managed=False
