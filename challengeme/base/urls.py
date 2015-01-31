from django.conf.urls import *
import challengeme.base.views as views 

urlpatterns = patterns('',
    url(r'^$', views.poop, name='poop'),
    url(r'^challenges$', views.AllChallengesView.as_view(), name='challenges'),
    # url(r'^challenges/id$', views.AllInstancesView.as_view(), name='instances'),

)
