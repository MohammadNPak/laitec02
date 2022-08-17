from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='user_profile')


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + "-" + slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title + " | " + self.author.user.username
