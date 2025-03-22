from django.contrib import admin
from .models import Job,Category,apply, State, Region
# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(apply)
admin.site.register(State)
admin.site.register(Region)