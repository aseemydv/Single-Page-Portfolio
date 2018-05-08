"""portfolio_design_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from onePgFolio import views
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    ## url(regex, view_function, kwargs, name)
    url(r'^admin/', admin.site.urls),
    path('', include('onePgFolio.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^sort_work_ex/$', views.sort_work_ex, name="sorted_exp"),
    url(r'^return_likes/$', views.liked_by, name="likes"),
    # url(r'^user_feedback/$', views.feedback, name="feedback"),
]
