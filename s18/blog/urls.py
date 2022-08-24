from django.urls import path, include
# from blog import urls as blog_urls
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/<slug:post_slug>', views.post, name='post'),
    path('api/test', views.api_test, name='api_test'),
    path('home/', TemplateView.as_view(
        template_name='blog/api_test.html'), name='home'),
]
