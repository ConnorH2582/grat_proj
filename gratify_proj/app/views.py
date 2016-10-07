from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from app.models import User,Event
import json
import requests
from django.utils.text import slugify

class CalendarView(View):
    def get(self,request,owner_id):


        calendar_owner = User.objects.filter(id=owner_id)[0]
        try:
            calendar_events = Event.objects.filter(owner=calendar_owner)
            # print(calendar_events)
            calendar_dict = {x.title: x.to_json() for x in calendar_events}
            return JsonResponse(calendar_dict)
        except IndexError:
            return JsonResponse({'error':'No Events'})


class CreateEventView(View):
    def post(self,request,owner_id):
        owner= User.objects.filter(id=owner_id)[0]
        title = request.POST.get('title')
        if request.POST.get('all_day'):
            all_day = True
        else:
            all_day = False
        
        start = request.POST.get('start')
        
        end = request.POST.get('end')

        if start > end:
            return JsonResponse({'Success':False,'error':'Your end date must come after your start date.'})
        
        attachment = request.FILES.get('attachment')

        new_event = Event.objects.get_or_create(owner=owner,title=title,all_day=all_day,start=start,end=end,attachment=attachment,slug=slugify(title))
        
        new_event_dict = new_event[0].to_json()

        return JsonResponse({'Success':True,'event':new_event_dict})


class EventIDView(View):
    def get(self,request,owner_id,event_slug):
        owner = User.objects.filter(id=owner_id)[0]
        event = Event.objects.filter(owner=owner,slug=event_slug)[0]
        return JsonResponse({'event_id':event.id})


class ShowEventView(View):
    def get(self,request,owner_id,event_id):
        owner = User.objects.filter(id=owner_id)[0]
        viewed_event = Event.objects.filter(owner=owner,id=event_id)[0]
        viewed_event_dict = viewed_event.to_json()
        return JsonResponse({'viewed_event_dict':viewed_event_dict})


