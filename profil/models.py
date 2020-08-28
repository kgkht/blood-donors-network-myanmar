from django.db import models
from phone_field import PhoneField
from Region.models import Address
from organizar.models import Organization

# Create your models here.

class Profil(models.Model):
    Blood_Types = [
            ('AMNS', "A -"),
            ('APLS', "A +"),
            ('BMNS', "B -"),
            ('BPLS', "B +"),
            ('ABMS', "AB -"),
            ('ABPS', "AB +"),
            ('OMNS', "O -"),
            ('OPLS', "O +"),
            ]
    name = models.CharField("Your Name",
                            max_length=50,
                            default="",
                            help_text="Enter Full Name")
    photo = models.ImageField("Profile Picture",
                              upload_to="images/profile",
                              blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    blood = models.CharField("Blood Type",
                             choices=Blood_Types,
                             max_length=4,
                             default="",
                             help_text="Choose Blood Type")
    address = models.OneToOneField(Address, on_delete=models.CASCADE,primary_key=True, blank=True, default="")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    last_donation = models.DateField("Donation Date", blank=True, auto_now=False, null=True)
    
    
    def __str__(self):
        return self.name