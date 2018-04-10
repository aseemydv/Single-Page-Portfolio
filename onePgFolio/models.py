from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone <-- no need,as there is nothing that require a timestamp

# Create your models here.
class experience(models.Model):
    co_name = models.CharField(max_length=20) ## nax_length argument is mandatory
    designation = models.CharField(max_length=20)
    project_description = models.TextField(max_length=500)
    worked_on = models.DateField()
    def __str__(self):
        return self.co_name


class social(models.Model):       
    social_links = models.URLField()
    social_img = models.ImageField() ## requires Pillow library