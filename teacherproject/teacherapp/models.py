from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    years_of_experience = models.IntegerField()
    profile_photo = models.FileField()

    def __str__(self):
        return self.first_name
