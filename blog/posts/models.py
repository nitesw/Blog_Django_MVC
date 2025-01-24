from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    image_url = models.CharField(default="", max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.likes} Likes"
