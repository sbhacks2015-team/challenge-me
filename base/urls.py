from django.conf.urls.defaults import *
# from models import AllTheRandomClasses TODO

from base import views

urlpatterns = patterns('',
    (r'^$', views.Poop.as_view())
)
