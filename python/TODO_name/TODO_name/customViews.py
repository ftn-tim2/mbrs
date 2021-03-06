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

from apps.settings import BASE_DIR
from TODO_name.models import Order
from TODO_name.models import City
from TODO_name.models import Invoice

#TODO implement missing methods
#url(r'^reportorders/$', 'TODO_name.customViews.reportorders', name='reportorders'),
#url(r'^reportinvoices/$', 'TODO_name.customViews.reportinvoices', name='reportinvoices'),
#url(r'^finish/$', 'TODO_name.customViews.finish', name='finish'),
#url(r'^createinvoice/$', 'TODO_name.customViews.createinvoice', name='createinvoice'),
#url(r'^cancel/$', 'TODO_name.customViews.cancel', name='cancel'),
#url(r'^cancel/$', 'TODO_name.customViews.cancel', name='cancel'),
#url(r'^copy/$', 'TODO_name.customViews.copy', name='copy'),


def copy(request):

    return response

def cancel(request):

    return response
 
def createinvoice(request):

    return response
 
def finish(request):

    return response

def reportinvoices(request):



    invoices  =  Invoice.objects.all()
    filename = "Invoices" +datetime.now().strftime('%B%d-%Y-%I-%M-%S%p') + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    c = canvas.Canvas(response)
    c.setFont('Helvetica-Bold', 10)
    c.setFillColorRGB(255,0,0)
    c.drawString(7*cm, 29*cm,  "Invoices")
    c.drawString(3*cm, 27*cm, "Invoice number")
    c.drawString(8*cm, 27*cm, "Date")
    c.drawString(12*cm, 27*cm, "Total")
    c.drawString(15*cm, 27*cm, "Status")
    c.setFillColorRGB(0,0,0)
    c.setFont('Helvetica', 8)
    row = 25
    for i in invoices:
        c.drawString(3*cm, row*cm, i.invoiceNumber.__str__())
        c.drawString(5*cm, row*cm, i.invoiceDate.__str__())
        c.drawString(12*cm, row*cm, i.invoiceTotal.__str__())
        c.drawString(15*cm, row*cm, i.canceled.__str__())
        row = row - 1
    c.save()
    return response 

def reportorders(request):

    orders  =  Order.objects.all()
    filename = "Order" +datetime.now().strftime('%B%d-%Y-%I-%M-%S%p') + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    c = canvas.Canvas(response)
    c.setFont('Helvetica-Bold', 10)
    c.setFillColorRGB(255,0,0)
    c.drawString(7*cm, 29*cm, "Orders")
    c.drawString(3*cm, 27*cm, "Order number")
    c.drawString(8*cm, 27*cm, "Date")
    c.drawString(12*cm, 27*cm, "Total")
    c.drawString(15*cm, 27*cm, "Status")
    c.setFillColorRGB(0,0,0)
    c.setFont('Helvetica', 8)
    row = 25
    for o in orders:
        c.drawString(3*cm, row*cm, o.orderNumber.__str__())
        c.drawString(5*cm, row*cm, o.orderDate.__str__())
        c.drawString(12*cm, row*cm, o.orderTotal.__str__())
        c.drawString(15*cm, row*cm, o.orderStatus.__str__())
        row = row - 1
    c.save()
    return response 

def report_week(request):

    cities  =  City.objects.all()
    filename = "Week" +datetime.now().strftime('%B%d-%Y-%I-%M-%S%p') + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    c = canvas.Canvas(response)
    orders = Order.objects.filter(orderDate__gte = datetime.now() - timedelta(days=7))
    c.setFont('Helvetica-Bold', 10)
    c.setFillColorRGB(255,0,0)        
    c.drawString(7*cm, 29*cm, "Orders week")
    c.drawString(3*cm, 27*cm, "Order number")
    c.drawString(8*cm, 27*cm, "Date")
    c.drawString(12*cm, 27*cm, "Total")
    c.drawString(15*cm, 27*cm, "Status")
    c.setFillColorRGB(0,0,0)
    c.setFont('Helvetica', 8)
    row = 25
    zarada = 0
    orders_city = []
    for city in cities:
        c.drawString(1*cm,row*cm, "*" + city.name.__str__())
        row = row - 1
        for order in orders:
            if(city.order == order):
                orders_city.append(order)
                
        for o in orders_city:
            c.drawString(3*cm, row*cm, o.orderNumber.__str__())
            c.drawString(5*cm, row*cm, o.orderDate.__str__())
            c.drawString(12*cm, row*cm, o.orderTotal.__str__())
            c.drawString(15*cm, row*cm, o.orderStatus.__str__())
            zarada = zarada + o.orderTotal
            row = row - 1
        c.setFillColorRGB(0,255,255)   
        c.drawString(1*cm, row*cm, "Total profit for city:" + zarada.__str__())
        c.setFillColorRGB(0,0,0)
        row = row - 1
        orders_city = []
        zarada = 0
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