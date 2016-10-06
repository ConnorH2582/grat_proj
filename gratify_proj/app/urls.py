from django.views.decorators.csrf import csrf_exempt   
from django.conf.urls import include, url
from django.contrib import admin
from app.views import CalendarView,CreateEventView,DeleteEventView,UpdateEventView
from django.views.generic import View


urlpatterns = [

 	# url(r'^(?P<username>[a-z0-9A-Z]{1,20})/id_view/$', ID_View.as_view(),name='id_view'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/show/$', CalendarView.as_view(),name='show_calendar'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/create/$', csrf_exempt(CreateEventView.as_view()),name='create_event'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/(?P<event_id>[0-9]+)/update/$', DeleteEventView.as_view(),name='delete_event'),

    url(r'^(?P<owner_id>[0-9]+)/calendar/events/(?P<event_id>[0-9]+)/delete$', UpdateEventView.as_view(),name='update_event'),

]