from django.db import models
class URL(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    short_url = models.CharField(max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)