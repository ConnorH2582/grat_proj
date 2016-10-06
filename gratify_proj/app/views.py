from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from app.models import User,Event
import json
import requests

# Create your views here.

class CalendarView(View):
    def get(self,request,owner_id):
        print(owner_id)
        calendar_owner = User.objects.filter(id=owner_id)[0]
        print(calendar_owner)
        try:
            calendar_events = Event.objects.filter(owner=calendar_owner)
            calendar_dict = [x.to_json() for x in calendar_events]
            return JsonResponse({'events':calendar_dict})
        except IndexError:
            return JsonResponse({'error':'No Events'})


class CreateEventView(View):
    def post(self,request,owner_id):
        print(request.POST)
        owner= User.objects.filter(id=owner_id)[0]
        print(owner)
        title = request.POST.get('title')
        print(title)

        if request.POST.get('all_day') == "True":
            all_day = True
        else:
            all_day = False
        
        start = request.POST.get('start')
        end = request.POST.get('end')
        attachment = request.FILES.get('attachment')


        new_event = Event.objects.get_or_create(owner=owner,title=title,all_day=all_day,start=start,end=end,attachment=attachment)

            
        new_event_dict = new_event[0].to_json()

        return JsonResponse({'Success':True,'event':new_event_dict})

class DeleteEventView(View):
    pass


class UpdateEventView(View):
    pass


