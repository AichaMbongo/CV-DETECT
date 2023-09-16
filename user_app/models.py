from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=20)
    sex = models.BooleanField()

    
    # Fields for 2FA
    otp_secret = models.CharField(max_length=16, null=True, blank=True)
    backup_codes = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def has_verified_2fa(self):
        return TOTPDevice.objects.filter(user=self, confirmed=True).exists()



        
    
    