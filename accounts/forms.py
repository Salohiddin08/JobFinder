from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django import forms
from .models import City, Region,Country


from accounts.models import Profile

class CountryForm(forms.ModelForm):
    class Meta:
        model=Country
        fields='__all__'

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['city','phone_number','image']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'region']
        
    region = forms.ModelChoiceField(queryset=Region.objects.all())
# forms.py
from django import forms

