from django.conf.urls import  include, url
from django.contrib import admin
from django.views.generic import View

urlpatterns = [
	url(r'^client/', include('client.urls', namespace = 'client', app_name = 'client')),

	url(r'^app/', include('app.urls', namespace = 'app', app_name = 'app')),

   url('', include('django.contrib.auth.urls', namespace='auth')),

	url('', include('social.apps.django_app.urls', namespace='social')),

	url(r'^admin/', include(admin.site.urls)),
]