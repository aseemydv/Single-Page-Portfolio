from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url('user_feedback/', views.emailView, name='email'),
]