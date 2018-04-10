from django.shortcuts import render
from django.conf.urls.static import static
#from .models import 
# Create your views here.

def home(request):
    return render(request, 'index.html')