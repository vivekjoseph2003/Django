from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=300)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
