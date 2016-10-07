from django.views.decorators.csrf import csrf_exempt   
from django.conf.urls import include, url
from django.contrib import admin
from app.views import CalendarView,CreateEventView,EventIDView,ShowEventView
from django.views.generic import View


urlpatterns = [

    url(r'^(?P<owner_id>[0-9]+)/calendar/show/$', CalendarView.as_view(),name='show_calendar'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/create/$', csrf_exempt(CreateEventView.as_view()),name='create_event'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/(?P<event_slug>[a-z0-9-]{1,100})/id_view/$', EventIDView.as_view(),name='event_id_view'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/(?P<event_id>[0-9]+)/show_event/$', ShowEventView.as_view(),name='show_event'),

]