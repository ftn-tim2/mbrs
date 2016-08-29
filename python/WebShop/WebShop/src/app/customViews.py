from _datetime import datetime
from datetime import timezone, timedelta
import json
import re

from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from WebShop.settings import BASE_DIR
from app.models import Order
from app.models import City



def report_week(request):

    cities  =  City.objects.all()
    for city in cities:
        orders = Order.objects.filter(orderDate__gte = datetime.now() - timedelta(days=7))
        filename = "Week" +datetime.now().strftime('%B%d-%Y-%I-%M-%S%p') + '.pdf'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

        c = canvas.Canvas(response)
        c.drawString(7*cm, 29*cm, "Orders week")
        c.drawString(1*cm, 28*cm, "*" + city.name.__str__())
        c.drawString(1*cm, 26*cm, "Order number")
        c.drawString(5*cm, 26*cm, "Date")
        c.drawString(12*cm, 26*cm, "Total")
        c.drawString(15*cm, 26*cm, "Status")
        row = 25
        zarada = 0
        for o in orders:
            if(o.city == city):
                c.drawString(1*cm, row*cm, o.orderNumber.__str__())
                c.drawString(5*cm, row*cm, o.orderDate.__str__())
                c.drawString(12*cm, row*cm, o.orderTotal.__str__())
                c.drawString(15*cm, row*cm, o.orderStatus.__str__())
                zarada = zarada + o.orderTotal
                row = row - 1
        c.drawString(1*cm, 27*cm, "Total profit for city:" + zarada.__str__())
        c.save()
        return response
    
def report_city(request):

    cities  =  City.objects.all()
    filename = "City" +datetime.now().strftime('%B%d-%Y-%I-%M-%S%p') + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    c = canvas.Canvas(response)
    row = 25
    for city in cities:
        c.drawString(1*cm, row*cm, city.name.__str__())
        c.drawString(5*cm, row*cm, city.zipCode.__str__())
        row = row - 1
    c.save()
    return response