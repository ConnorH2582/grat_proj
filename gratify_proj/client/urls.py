from django.conf.urls import include, url
from django.views.generic import View
from client.views import IndexView,EventView

urlpatterns = [

	url(r'^index/$', IndexView.as_view(), name='index'),

    url(r'^(?P<username>[a-z0-9A-Z]+)/events/(?P<event_slug>[a-z0-9-]{1,100})/$', EventView.as_view(),name='event_view'),

]

