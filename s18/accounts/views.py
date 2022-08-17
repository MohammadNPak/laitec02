
from django.db import reset_queries
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import (authenticate,
                                 login as django_login,
                                 logout as django_logout)
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user=user)
                messages.add_message(
                    request, messages.SUCCESS, 'you have loged in successfully!')
            else:
                messages.add_message(
                    request, messages.ERROR, 'username or password is wrong!')
            return render(request, 'message.html')
    elif request.method == "GET":
        if request.user.is_authenticated:
            messages.add_message(request, messages.SUCCESS,
                                 'you have been loged in already!')
            return render(request, 'accounts/login-successful.html', {})
        return render(request, 'accounts/login.html', {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():

            user = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 f'registered {user.username} successfully')

            return render(request, 'message.html', {})
        else:
            return render(request, 'accounts/register.html', {"form": form})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {"form": form})


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        messages.add_message(request, messages.SUCCESS,
                             'you have been loged out successfully!')
        return render(request, 'message.html', {})
    return redirect(reverse('login'))


def add_education(request):
    return render(request, 'accounts/add-education.html', {})


def add_education(request):
    return render(request, 'accounts/add-education.html', {})


def create_profile(request):
    return render(request, 'accounts/create_profile.html', {})


def profiles(request):
    return render(request, 'accounts/profiles.html', {})


def profile(request):
    return render(request, 'accounts/profile.html', {})


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def add_experience(request):
    return render(request, 'accounts/add-experience.html', {})
