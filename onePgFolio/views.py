from django.shortcuts import render
from .models import experience, social
import re
#from .models import 
# Create your views here.

def index(request):
    work_ex = experience.objects.all()
    icons = social.objects.all()
    alt_text = []
    for i in icons:
        alt_text.append(re.findall(r'//([w|in]+.)?(\w+).',i.social_links)[0][1])
    both = zip(icons, alt_text)
    return render(request, 'index.html', {'work_ex':work_ex, 'both':both})