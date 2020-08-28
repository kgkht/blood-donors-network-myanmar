from django.contrib import admin
from .models import Organization
from Region.models import Address

# Register your models here.


admin.site.register(Organization)
admin.site.register(Address)