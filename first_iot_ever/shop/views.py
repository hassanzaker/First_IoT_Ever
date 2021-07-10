# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('OK', status=200)

def shop(request):
    return render(request, 'shop/shop.html', context={})