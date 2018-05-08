from django.db import models
from django.contrib.auth.models import User
from django.forms import ComboField
from django import forms
import re

# from django.utils import timezone <-- no need,as there is nothing that require a timestamp

# Create your models here.
# MultiValueField - knows that model's one field contains multiple values
# MultiWidget     - knows how each discrete values must be presented
# class Meta      - container for configuration attributes of the outer class. In peewee (and also Django), the attributes of a class 
#                   (for those that inherit from Model) are expect to be fields that correspond to their counterparts in the database. 
#                   How then to add attributes that aren't database fields? The Meta class is the container for these non-field attributes.
#                   As new instances of your outer class are created, the class constructor will look to the Meta attribute for specific configuration details.
# django docs     - https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options

class experience(models.Model):
    co_name = models.CharField(help_text='Enter company name', max_length=20) ## nax_length argument is mandatory
    designation = models.CharField(help_text='Enter your designation there', max_length=20)
    project_description = models.TextField(help_text='Care to describe what you did there..', max_length=500)
    worked_on = models.DateField()
    def __str__(self):
        return self.co_name


class social(models.Model):       
    social_links = models.URLField()
    social_img = models.ImageField() ## requires Pillow library    
    def __str__(self):
        return re.findall(r'//([w|in]+.)?(\w+).',self.social_links)[0][1]

class appreciate(models.Model):
    likes = models.IntegerField(default=0)
    def __str__(self):
        return "Likes"

class file_save(models.Model):
    resume = models.FileField()

class get_feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    remarks = models.TextField(max_length=400)

    def __str__(self):
        return str(self.email)

