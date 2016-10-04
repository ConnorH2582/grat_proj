from django.conf.urls import patterns, include, url
from django.views.generic import View

urlpatterns = patterns('',

url(r'^/home/$', HomeView.as_view(),name='home'),

)

