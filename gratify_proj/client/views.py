from django.shortcuts import render,redirect
from django.template.context import RequestContext
from django.views.generic import View
from app.models import User, Event
import requests


class IndexView(View):
	template='client/index.html'
	def get(self,request):
		context = {'request':request,'user': request.user}
		if not request.user.is_anonymous():
			# active_user_id = request.user.id
			# user_calendar_url = 'http://myapp.com:8000/app/{}/calendar/show/'
			# r = requests.get(user_calendar_url)

			return render(request,self.template,context)
		return render(request,self.template,context)

