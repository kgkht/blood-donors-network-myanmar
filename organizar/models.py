from django.db import models
from phone_field import PhoneField
from Region.models import Address
# Create your models here.

class Organization(models.Model):
    name = models.CharField("Org Name", help_text="Your organization name", max_length=30)
    logo = models.ImageField('Upload Your Logo', upload_to='images/logo/')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.name