from django.shortcuts import render,redirect
from django.template.context import RequestContext
from django.views.generic import View
from app.models import User, Event
from app.forms import EventForm
import requests


class IndexView(View):
    template='client/index.html'
    event_form = EventForm()
    def get(self,request):
        context = {'request':request,'user': request.user,'event_form':self.event_form}
        if not request.user.is_anonymous():
            active_user_id = request.user.id
            user_calendar_url = 'http://myapp.com:8000/app/{}/calendar/show/'.format(active_user_id)
            r = requests.get(user_calendar_url)
            

            return render(request,self.template,context)
        return render(request,self.template,context)

    def post(self,request):
        if not request.user.is_anonymous():
            active_user_id = request.user.id
            url = "http://myApp.com:8000/app/{}/calendar/events/create/".format(active_user_id)
            submitted_event = EventForm(request.POST)
        
            if submitted_event.is_valid():
                title = submitted_event.cleaned_data.get('title')
                start = submitted_event.cleaned_data.get('start')
                end = submitted_event.cleaned_data.get('end')
                all_day = request.POST.get('all_day')
                
                payload = {'title':title,'start':start,'end':end,'all_day':all_day}
                if request.FILES:

                    r = requests.post(url,files=request.FILES,data=payload)
                else:
                    r = requests.post(url,data=payload)

                if r.json().get('Success'):
                    return redirect('client:index')
                else:
                    return redirect('client:index')

class EventView(View):
    template='client/eventview.html'
    def get(self, request, username, event_slug):
        if not request.user.is_anonymous():
            active_user_id = request.user.id
            url = 'http://myApp.com:8000/app/{}/calendar/events/{}/id_view/'.format(active_user_id,event_slug)
            r = requests.get(url)
            event_id = r.json().get('event_id')

            url = 'http://myApp.com:8000/app/{}/calendar/events/{}/show_event/'.format(active_user_id,event_id)
            r = requests.get(url)
           
            event_dict = r.json().get('viewed_event_dict')

            context = {'user': request.user,'event':event_dict}

            return render(request, self.template,context)
            
            
