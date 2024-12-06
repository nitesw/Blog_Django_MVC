from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.likes} Likes"