from django.contrib import admin
from .models import experience, social, appreciate, get_feedback

# Register your models here.
admin.site.register(experience)
admin.site.register(social)
admin.site.register(appreciate)
admin.site.register(get_feedback)