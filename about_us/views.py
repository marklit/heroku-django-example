# -*- coding: utf-8 -*-
from about_us.models import Person, Role
from about_us.tasks import CheckPersonTask
from base.utils import is_mobile_browser
from django.http import (HttpResponseBadRequest, Http404, HttpResponse, 
    HttpResponseRedirect)
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
    try:
        user_agent = request.META['HTTP_USER_AGENT']
    except KeyError:
        user_agent = ""
    
    interaction = 'touch' if is_mobile_browser(user_agent) else 'click'
    
    return render_to_response('about_us/home.%s.html' % interaction, { 
        'people_list': Person.objects.filter(is_published=True)[:5] })

def check_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    
    CheckPersonTask.delay(person.id)
    
    return HttpResponse("Will check person %d in a moment." % person.id)