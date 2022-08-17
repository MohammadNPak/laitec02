from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('add_education', views.add_education, name='add_education'),
    path('add_experience', views.add_experience, name='add_experience'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),

    path('profiles', views.profiles, name='profiles'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('logout', views.logout, name='logout'),
]
