from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, 'accounts/login.html', {})


def add_education(request):
    return render(request, 'accounts/add-education.html', {})


def add_experience(request):
    return render(request, 'accounts/add-experience.html', {})


def create_profile(request):
    return render(request, 'accounts/create-profile.html', {})


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def index(request):
    return render(request, 'accounts/index.html', {})


def profile(request):
    return render(request, 'accounts/profile.html', {})


def profiles(request):
    return render(request, 'accounts/profiles.html', {})


def register(request):
    return render(request, 'accounts/register.html', {})
