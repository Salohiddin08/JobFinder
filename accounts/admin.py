# accounts/admin.py
from django.contrib import admin
from .models import Country, Region, City, Profile

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Profile)
