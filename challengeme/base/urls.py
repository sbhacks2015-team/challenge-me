from django.conf.urls import *
import challengeme.base.views as views 

urlpatterns = patterns('',
    url(r'^$', views.poop, name='poop'),
    url(r'^challenge$', views.AllChallengesView.as_view(), name='challenge'),
    # url(r'^challenge/
)
