from django.conf.urls import include, url
from django.views.generic import View
from client.views import IndexView

urlpatterns = [

	url(r'^index/$', IndexView.as_view(), name='index'),

]

