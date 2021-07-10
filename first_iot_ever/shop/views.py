from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from . import models
import random

# Create your views here.

def shop(requset):
    items = models.Item.objects.all()
    return render(requset, 'shop.html', {'item1': items[0], 'item2': items[1]})


def reserve(requset, slot):
    item = models.Item.objects.all()[slot - 1]
    if item.count <= 0:
        return HttpResponseBadRequest('There is no item available to reserve!') 
    ticket = random.randrange(1000, 9999)
    while models.Ticket.objects.filter(id=ticket):
            ticket = random.randrange(1000, 9999)
    t = models.Ticket(id = ticket, slot=slot)
    t.save()
    item.count = item.count - 1
    item.save()
    return render(requset, 'reserve.html', {'ticket': ticket})

def validate_reserveation(request, ticket):
    t = models.Ticket.objects.filter(id = ticket)
    if t:
        temp = str(t[0].slot)
        t.delete()
        return HttpResponse(temp)
    else:
        return HttpResponseBadRequest('INVALID')

def get_item(request, slot):
    item = models.Item.objects.all()[slot - 1]
    if item.count <= 0:
        return HttpResponseBadRequest('There is no item available to reserve!') 
    item.count = item.count - 1
    item.save()
    return HttpResponse('Done')


def update_tempereture(request, slot, tempereture):
    item = models.Item.objects.all()[slot - 1]
    item.tempereture = float(tempereture)
    item.save()
    return HttpResponse('Done')


def payment(request, cardid, password):
    if password == cardid:
        return HttpResponse('Done')
    else:
        return HttpResponseBadRequest('Wrong info')