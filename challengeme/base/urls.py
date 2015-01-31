from django.conf.urls import *
import challengeme.base.views as views 

urlpatterns = patterns('',
    url(r'^$', views.poop, name='poop'),
)
