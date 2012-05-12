# -*- coding: utf-8 -*-
from about_us.models import Person, Role
from about_us.tasks import CheckPersonTask
from django.http import (HttpResponseBadRequest, Http404, HttpResponse, 
    HttpResponseRedirect)
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
    return render_to_response('about_us/home.html', { 'people_list': 
        Person.objects.filter(is_published=True)[:5] })

def check_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    CheckPersonTask.delay(person.id)
    return HttpResponse("Will check person %d in a moment." % person.id)