from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.hashers import make_password, check_password

    
class CustomUser(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_country = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_profile_photo = models.FileField(upload_to='profile_photos/', null=True, blank=True)
    user_address_line_1 = models.CharField()
    user_password = models.CharField()
    # last_login=models.DateTimeField()
    user_status=models.BooleanField(default=False)
    user_hold=models.BooleanField(default=False)
    # user_joined_date = models.DateField()
    # user_address_line_2 = models.CharField()
    user_type = models.CharField()
    user_state= models.CharField()
    user_pin_code=models.CharField()
    profile_privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')
    def save(self, *args, **kwargs):
            # Hash the password if it's not already hashed
            if not self.pk or not self.user_password.startswith('pbkdf2_sha256$'):
                self.user_password = make_password(self.user_password)

            # Call the save method of the parent class
            super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the raw_password matches the hashed password in the database
        return check_password(raw_password, self.user_password)
    class Meta:
        db_table = 'users' 
        managed=False
