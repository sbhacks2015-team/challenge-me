from django.conf.urls import *
import challengeme.base.views as views 
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.poop, name='poop'),
    url(r'^login/$', 
        'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}),
    url(r'^challenges$', 
        login_required(views.AllChallengesView.as_view()),
        name='challenges'),
    url(r'^challenges/(?P<pk>\d+)/$',
        login_required(views.ChallengeDetailView.as_view()),
        name='challenge'),
#    url(r'^go/$',
#        login_required(views.AllInstancesView.as_view()),
#        name='instances'),
#    url(r'^go/(?P<instance_id>\d+)/$',
#        login_required(views.InstanceView.as_view()),
#        name='instance'),
)
