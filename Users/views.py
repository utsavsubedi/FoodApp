from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def UserLogin(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success( request, f"Congratulations {username}! Your account is sucessfully created." )
            return redirect('food:index')
    else:   
        form =  UserForm()
    return render( request, 'Users/UserLogin.html',  { "form":form } )

@login_required
def UserProfile(request):
    return render( request, 'Users/profile.html' )
