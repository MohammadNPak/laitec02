from django.urls import path
from . import views
urlpatterns = [
    path('education/', views.add_education, name='education'),
    path('experience/', views.add_experience, name='experience'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

]
