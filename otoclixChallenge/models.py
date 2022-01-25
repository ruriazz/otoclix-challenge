from django.db import models

# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)