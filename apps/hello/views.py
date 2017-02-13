# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Contact


def home(request):
    contact = Contact.objects.first()
    return render(request, 'hello/home.html', {'info': contact})
