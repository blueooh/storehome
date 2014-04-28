from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect, get_object_or_404
from intro.models import Menu, ScheduleEvents
import json

def home(request):
    m = Menu.objects.filter(distiction=1)[:4]
    return render_to_response('index.html', {'view': 'home', 'menu_list': m})

def menu(request):
    m = Menu.objects.all()
    return render_to_response('menu_list.html', {'view': 'menu', 'menu_list': m})

def favorate(request):
    m = Menu.objects.filter(distiction=1)
    return render_to_response('menu_list.html', {'view': 'menu', 'menu_list': m})

def reservation_menu(request):
    m = Menu.objects.filter(distiction=2)
    return render_to_response('menu_list.html', {'view': 'menu', 'menu_list': m})

def contact(request):
    return render_to_response('contact.html', {'view': 'contact'})

def schedule(request):
    return render_to_response('schedule.html', {'view': 'schedule'})

def schedule_events(request):
    sche = ScheduleEvents.objects.all()

    resp = {}
    resp['success'] = 1
    resp['result'] = []

    for s in sche:
        d = {}
        d['id'] = s.id
        d['title'] = s.title
        d['url'] = s.url
        d['class'] = s.css_class
        d['start'] = s.start_timestamp
        d['end'] = s.end_timestamp
        resp['result'].append(d)

    return HttpResponse(json.dumps(resp), content_type="application/json")
