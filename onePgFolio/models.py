from django.db import models
from django.contrib.auth.models import User
from django.forms import ComboField
from django import forms
# from django.utils import timezone <-- no need,as there is nothing that require a timestamp

# Create your models here.
class PhoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            models.CharField(),
            models.DateField(),
        )
        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )

class experience(models.Model, PhoneField):
    co_name = models.CharField(max_length=20) ## nax_length argument is mandatory
    designation = models.CharField(max_length=20)
    project_description = models.TextField(max_length=500)
    worked_on = models.DateField()

    def __str__(self):
        return self.co_name


class social(models.Model):       
    social_links = models.URLField()
    social_img = models.ImageField() ## requires Pillow library