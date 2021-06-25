from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')
        return redirect("home")
    else:
        return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid creditials')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect("login")
