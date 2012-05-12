# -*- coding: utf-8 -*-
from about_us.models import Person, Role
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('about_us/home.html', { 'people_list': 
        Person.objects.filter(is_published=True)[:5] })