from django.urls import path, include
# from blog import urls as blog_urls
from . import views
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/<slug:post_slug>', views.post, name='post'),
]
