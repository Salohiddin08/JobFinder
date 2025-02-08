from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
from .countries_list import countries 

def logout_view(request):
    logout(request)  
    return render(request, 'home/homepage.html') 




# Register view
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():  
            
            user = form.save()
            
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            

            user = authenticate(username=username, password=password)
            if user is not None:
                
                login(request, user)
                return redirect('/accounts/profile')  
            else:

                return render(request, 'registration/signup.html', {
                    'signupform': form,
                    'error': 'Authentication failed. Please try logging in.'
                })
        else:
            
            print(form.errors)
    else:
        
        form = SignupForm()

    
    return render(request, 'registration/signup.html', {'signupform': form})




def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    return render(request, 'accounts/profile.html', {'profile': profile})




def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile_form=profile_form.save(commit=False)
            myprofile_form.user = request.user
            myprofile_form.save()

            return redirect(reverse('accounts:profile'))

    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=profile)



    return render(request,'accounts/profile_edit.html',{"User_Form":user_form,"Profile_Form":profile_form})


def country_view(request):
    return render(request, 'your_template.html', {'countries': countries})
