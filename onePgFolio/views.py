from django.shortcuts import render
from django.shortcuts import redirect
from .models import experience, social, appreciate, get_feedback
from .forms import get_to_know
import re
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
import django
from django.core.mail import send_mail

#from .models import 
# Create your views here.

def index(request):
    # return a list of work exp. in reverse chronological order
    work_ex = toggle_order('asc') ## View work experience orderedin reverse chronological order
    icons = social.objects.all()
    alt_text = []
    for i in icons:
        alt_text.append(re.findall(r'//([w|in]+.)?(\w+).',i.social_links)[0][1])
    both = zip(icons, alt_text)
    gtk = get_to_know()
    return render(request, 'index.html', {'work_ex':work_ex, 'both':both, 'gtk':gtk })

def sort_work_ex(request):
    ''' will yield the list of work experience to
    sort in descending order (chronological order)
    when checkbox is clicked'''
    if request.is_ajax():
        ord = request.GET.get('mydata','')        
        s_work_ex = toggle_order(ord) ## View work experience ordered in reverse chronological order        
    else:
        s_work_ex = 'failed to received AJAX request'
    swe = serializers.serialize('json',s_work_ex)
    mimetime = 'application/json'
    #return HttpResponse(swe, mimetime)
    return render(request, 'resume.html', {'work_ex':s_work_ex})

def toggle_order(ord):    
    if ord == 'asc':
        work_ex = experience.objects.filter().order_by('-worked_on')    
        description = "User chose to print in Reverse-chronological Order"    
    else:
        work_ex = experience.objects.filter().order_by('worked_on')    
        description = "User chose to print in Chronological Order"        
    return work_ex
    
def liked_by(request):
    app = appreciate.objects.get(id=1)
    if request.is_ajax():
        likes = 0
        if request.method == 'GET':
            print("user's IP: "+str(request.META.get('REMOTE_ADDR')))
            likes = app.likes + 1
        app.likes = likes
        app.save()    
    likes = app.likes
    return HttpResponse(likes)
    #return render(request, 'like_counter.html', {'likes': app.likes})

def feedback(request):       
    if request.method == "POST":
        fform = get_to_know(request.POST)
        if fform.is_valid():
            name = fform.cleaned_data['name']
            email = fform.cleaned_data['email']
            remarks = fform.cleaned_data['remarks']
            gtk = get_to_know({'name':name, 'email':email, 'remarks':remarks})    
            gtk.save(commit=True) 
    else:
        gtk = get_to_know()    
    return redirect('index')

def emailView(request):
    if request.method == 'GET':
        gtk = get_to_know()
    else:
        ## recieved POST method
        feedForm = get_to_know(request.POST)
        if feedForm.is_valid():
            name = feedForm.cleaned_data['name']
            email = feedForm.cleaned_data['email']
            remarks = feedForm.cleaned_data['remarks']
            print("$$$$$"+str(feedForm.cleaned_data))
            ## send_email(
            #    'subject goes here',
            #    'message',
            #    'from@abc.def'
            #    ['to@abc.def', ]
            #    fail_silently =  False,
            # )
            try:
                send_mail('', remarks, email, ['admin@example.com'])
            except Exception as e:
                print("Error %s thrown"%str(e))
                return HttpResponse('Invalid header found')
    return redirect('index')