from _datetime import datetime
import json
import re

from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib import messages


from app.forms import CityForm, EnterpriseForm, StateForm, DepartmentForm, VendorForm, OrderItemForm, OrderForm, PriceListItemForm, PaymentForm, InvoiceForm, CustomerForm, PriceListForm, StockForm, ProductForm, CategoryForm, StockKeepingUnitForm
from app.models import City, Enterprise, State, Department, Vendor, OrderItem, Order, PriceListItem, Payment, Invoice, Customer, PriceList, Stock, Product, Category, StockKeepingUnit


def list_city(request):
    context = RequestContext(request)
    citys = City.objects.all()
    
    return render_to_response('app/cityList.html',{'deletable' : "true", "citys" : citys},context)
    
def city(request, city_id):
    context = RequestContext(request)
    city_form = CityForm(instance=City.objects.get(pk=city_id))  
    
    enterprises = Enterprise.objects.filter(city=City.objects.get(pk=city_id))
    departments = Department.objects.filter(city=City.objects.get(pk=city_id))
    vendors = Vendor.objects.filter(city=City.objects.get(pk=city_id))
    orders = Order.objects.filter(city=City.objects.get(pk=city_id))
    customers = Customer.objects.filter(city=City.objects.get(pk=city_id))
    return render_to_response('app/city.html',{'cityForm': city_form, 'city_id': city_id, 'editable' : 'true', 'enterprises' : enterprises, 'departments' : departments, 'vendors' : vendors, 'orders' : orders, 'customers' : customers}, context)
    
def add_city(request):
    context = RequestContext(request)
    if request.method == 'POST':
        city_form = CityForm(data=request.POST)
        if city_form.is_valid():
            city = city_form.save()
            city.save()
            
            return render_to_response('app/city.html',{"cityForm" : city_form},context)    
        else: 
            messages.error(request, city_form.errors)
    else:
        city_form = CityForm()
        
        enterprises = Enterprise.objects.all()
        departments = Department.objects.all()
        vendors = Vendor.objects.all()
        orders = Order.objects.all()
        customers = Customer.objects.all()
    return render_to_response('app/cityAdd.html', {'cityForm': city_form, 'enterprises' : enterprises, 'departments' : departments, 'vendors' : vendors, 'orders' : orders, 'customers' : customers}, context)
    
    
def modify_city(request, city_id):
    context = RequestContext(request)
    cityFromDB = City.objects.get(pk=city_id)
    if request.method == 'POST':
        city_form = CityForm(request.POST, instance=cityFromDB)
        if city_form.is_valid():
            city = city_form.save()
            city.save()
            
            enterprises = Enterprise.objects.filter(city=City.objects.get(pk=city_id))
            departments = Department.objects.filter(city=City.objects.get(pk=city_id))
            vendors = Vendor.objects.filter(city=City.objects.get(pk=city_id))
            orders = Order.objects.filter(city=City.objects.get(pk=city_id))
            customers = Customer.objects.filter(city=City.objects.get(pk=city_id))
            return render_to_response('app/city.html', {'cityForm': city_form, 'enterprises' : enterprises, 'departments' : departments, 'vendors' : vendors, 'orders' : orders, 'customers' : customers, 'city_id': city_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, city_form.errors)
        
    city_form = CityForm(instance=cityFromDB)
    return render_to_response('app/cityAdd.html', {'cityForm': city_form}, context)
            
def delete_city(request, city_id):
    context = RequestContext(request)
    city = City.objects.get(pk=city_id)
    if request.method == 'POST':
        city.delete();
        
    citys = City.objects.all()    
    return render_to_response('app/cityList.html',{"citys" : citys},context)
    

def list_enterprise(request):
    context = RequestContext(request)
    enterprises = Enterprise.objects.all()
    
    return render_to_response('app/enterpriseList.html',{'deletable' : "true", "enterprises" : enterprises},context)
    
def enterprise(request, enterprise_id):
    context = RequestContext(request)
    enterprise_form = EnterpriseForm(instance=Enterprise.objects.get(pk=enterprise_id))  
    
    departments = Department.objects.filter(enterprise=Enterprise.objects.get(pk=enterprise_id))
    return render_to_response('app/enterprise.html',{'enterpriseForm': enterprise_form, 'enterprise_id': enterprise_id, 'editable' : 'true', 'departments' : departments}, context)
    
def add_enterprise(request):
    context = RequestContext(request)
    if request.method == 'POST':
        enterprise_form = EnterpriseForm(data=request.POST)
        if enterprise_form.is_valid():
            enterprise = enterprise_form.save()
            enterprise.save()
            
            return render_to_response('app/enterprise.html',{"enterpriseForm" : enterprise_form},context)    
        else: 
            messages.error(request, enterprise_form.errors)
    else:
        enterprise_form = EnterpriseForm()
        
        departments = Department.objects.all()
    return render_to_response('app/enterpriseAdd.html', {'enterpriseForm': enterprise_form, 'departments' : departments}, context)
    
    
def modify_enterprise(request, enterprise_id):
    context = RequestContext(request)
    enterpriseFromDB = Enterprise.objects.get(pk=enterprise_id)
    if request.method == 'POST':
        enterprise_form = EnterpriseForm(request.POST, instance=enterpriseFromDB)
        if enterprise_form.is_valid():
            enterprise = enterprise_form.save()
            enterprise.save()
            
            departments = Department.objects.filter(enterprise=Enterprise.objects.get(pk=enterprise_id))
            return render_to_response('app/enterprise.html', {'enterpriseForm': enterprise_form, 'departments' : departments, 'enterprise_id': enterprise_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, enterprise_form.errors)
        
    enterprise_form = EnterpriseForm(instance=enterpriseFromDB)
    return render_to_response('app/enterpriseAdd.html', {'enterpriseForm': enterprise_form}, context)
            
def delete_enterprise(request, enterprise_id):
    context = RequestContext(request)
    enterprise = Enterprise.objects.get(pk=enterprise_id)
    if request.method == 'POST':
        enterprise.delete();
        
    enterprises = Enterprise.objects.all()    
    return render_to_response('app/enterpriseList.html',{"enterprises" : enterprises},context)
    

def list_state(request):
    context = RequestContext(request)
    states = State.objects.all()
    
    return render_to_response('app/stateList.html',{'deletable' : "true", "states" : states},context)
    
def state(request, state_id):
    context = RequestContext(request)
    state_form = StateForm(instance=State.objects.get(pk=state_id))  
    
    citys = City.objects.filter(state=State.objects.get(pk=state_id))
    return render_to_response('app/state.html',{'stateForm': state_form, 'state_id': state_id, 'editable' : 'true', 'citys' : citys}, context)
    
def add_state(request):
    context = RequestContext(request)
    if request.method == 'POST':
        state_form = StateForm(data=request.POST)
        if state_form.is_valid():
            state = state_form.save()
            state.save()
            
            return render_to_response('app/state.html',{"stateForm" : state_form},context)    
        else: 
            messages.error(request, state_form.errors)
    else:
        state_form = StateForm()
        
        citys = City.objects.all()
    return render_to_response('app/stateAdd.html', {'stateForm': state_form, 'citys' : citys}, context)
    
    
def modify_state(request, state_id):
    context = RequestContext(request)
    stateFromDB = State.objects.get(pk=state_id)
    if request.method == 'POST':
        state_form = StateForm(request.POST, instance=stateFromDB)
        if state_form.is_valid():
            state = state_form.save()
            state.save()
            
            citys = City.objects.filter(state=State.objects.get(pk=state_id))
            return render_to_response('app/state.html', {'stateForm': state_form, 'citys' : citys, 'state_id': state_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, state_form.errors)
        
    state_form = StateForm(instance=stateFromDB)
    return render_to_response('app/stateAdd.html', {'stateForm': state_form}, context)
            
def delete_state(request, state_id):
    context = RequestContext(request)
    state = State.objects.get(pk=state_id)
    if request.method == 'POST':
        state.delete();
        
    states = State.objects.all()    
    return render_to_response('app/stateList.html',{"states" : states},context)
    

def list_department(request):
    context = RequestContext(request)
    departments = Department.objects.all()
    
    return render_to_response('app/departmentList.html',{'deletable' : "true", "departments" : departments},context)
    
def department(request, department_id):
    context = RequestContext(request)
    department_form = DepartmentForm(instance=Department.objects.get(pk=department_id))  
    
    stocks = Stock.objects.filter(department=Department.objects.get(pk=department_id))
    return render_to_response('app/department.html',{'departmentForm': department_form, 'department_id': department_id, 'editable' : 'true', 'stocks' : stocks}, context)
    
def add_department(request):
    context = RequestContext(request)
    if request.method == 'POST':
        department_form = DepartmentForm(data=request.POST)
        if department_form.is_valid():
            department = department_form.save()
            department.save()
            
            return render_to_response('app/department.html',{"departmentForm" : department_form},context)    
        else: 
            messages.error(request, department_form.errors)
    else:
        department_form = DepartmentForm()
        
        stocks = Stock.objects.all()
    return render_to_response('app/departmentAdd.html', {'departmentForm': department_form, 'stocks' : stocks}, context)
    
    
def modify_department(request, department_id):
    context = RequestContext(request)
    departmentFromDB = Department.objects.get(pk=department_id)
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST, instance=departmentFromDB)
        if department_form.is_valid():
            department = department_form.save()
            department.save()
            
            stocks = Stock.objects.filter(department=Department.objects.get(pk=department_id))
            return render_to_response('app/department.html', {'departmentForm': department_form, 'stocks' : stocks, 'department_id': department_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, department_form.errors)
        
    department_form = DepartmentForm(instance=departmentFromDB)
    return render_to_response('app/departmentAdd.html', {'departmentForm': department_form}, context)
            
def delete_department(request, department_id):
    context = RequestContext(request)
    department = Department.objects.get(pk=department_id)
    if request.method == 'POST':
        department.delete();
        
    departments = Department.objects.all()    
    return render_to_response('app/departmentList.html',{"departments" : departments},context)
    

def list_vendor(request):
    context = RequestContext(request)
    vendors = Vendor.objects.all()
    
    return render_to_response('app/vendorList.html',{'deletable' : "true", "vendors" : vendors},context)
    
def vendor(request, vendor_id):
    context = RequestContext(request)
    vendor_form = VendorForm(instance=Vendor.objects.get(pk=vendor_id))  
    
    products = Product.objects.filter(vendor=Vendor.objects.get(pk=vendor_id))
    return render_to_response('app/vendor.html',{'vendorForm': vendor_form, 'vendor_id': vendor_id, 'editable' : 'true', 'products' : products}, context)
    
def add_vendor(request):
    context = RequestContext(request)
    if request.method == 'POST':
        vendor_form = VendorForm(data=request.POST)
        if vendor_form.is_valid():
            vendor = vendor_form.save()
            vendor.save()
            
            return render_to_response('app/vendor.html',{"vendorForm" : vendor_form},context)    
        else: 
            messages.error(request, vendor_form.errors)
    else:
        vendor_form = VendorForm()
        
        products = Product.objects.all()
    return render_to_response('app/vendorAdd.html', {'vendorForm': vendor_form, 'products' : products}, context)
    
    
def modify_vendor(request, vendor_id):
    context = RequestContext(request)
    vendorFromDB = Vendor.objects.get(pk=vendor_id)
    if request.method == 'POST':
        vendor_form = VendorForm(request.POST, instance=vendorFromDB)
        if vendor_form.is_valid():
            vendor = vendor_form.save()
            vendor.save()
            
            products = Product.objects.filter(vendor=Vendor.objects.get(pk=vendor_id))
            return render_to_response('app/vendor.html', {'vendorForm': vendor_form, 'products' : products, 'vendor_id': vendor_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, vendor_form.errors)
        
    vendor_form = VendorForm(instance=vendorFromDB)
    return render_to_response('app/vendorAdd.html', {'vendorForm': vendor_form}, context)
            
def delete_vendor(request, vendor_id):
    context = RequestContext(request)
    vendor = Vendor.objects.get(pk=vendor_id)
    if request.method == 'POST':
        vendor.delete();
        
    vendors = Vendor.objects.all()    
    return render_to_response('app/vendorList.html',{"vendors" : vendors},context)
    

def list_orderItem(request):
    context = RequestContext(request)
    orderItems = OrderItem.objects.all()
    
    return render_to_response('app/orderItemList.html',{'deletable' : "true", "orderItems" : orderItems},context)
    
def orderItem(request, orderItem_id):
    context = RequestContext(request)
    orderItem_form = OrderItemForm(instance=OrderItem.objects.get(pk=orderItem_id))  
    
    return render_to_response('app/orderItem.html',{'orderItemForm': orderItem_form, 'orderItem_id': orderItem_id, 'editable' : 'true'}, context)
    
def add_orderItem(request):
    context = RequestContext(request)
    if request.method == 'POST':
        orderItem_form = OrderItemForm(data=request.POST)
        if orderItem_form.is_valid():
            orderItem = orderItem_form.save()
            orderItem.save()
            
            return render_to_response('app/orderItem.html',{"orderItemForm" : orderItem_form},context)    
        else: 
            messages.error(request, orderItem_form.errors)
    else:
        orderItem_form = OrderItemForm()
        
    return render_to_response('app/orderItemAdd.html', {'orderItemForm': orderItem_form}, context)
    
    
def modify_orderItem(request, orderItem_id):
    context = RequestContext(request)
    orderItemFromDB = OrderItem.objects.get(pk=orderItem_id)
    if request.method == 'POST':
        orderItem_form = OrderItemForm(request.POST, instance=orderItemFromDB)
        if orderItem_form.is_valid():
            orderItem = orderItem_form.save()
            orderItem.save()
            
            return render_to_response('app/orderItem.html', {'orderItemForm': orderItem_form, 'orderItem_id': orderItem_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, orderItem_form.errors)
        
    orderItem_form = OrderItemForm(instance=orderItemFromDB)
    return render_to_response('app/orderItemAdd.html', {'orderItemForm': orderItem_form}, context)
            
def delete_orderItem(request, orderItem_id):
    context = RequestContext(request)
    orderItem = OrderItem.objects.get(pk=orderItem_id)
    if request.method == 'POST':
        orderItem.delete();
        
    orderItems = OrderItem.objects.all()    
    return render_to_response('app/orderItemList.html',{"orderItems" : orderItems},context)
    

def list_order(request):
    context = RequestContext(request)
    orders = Order.objects.all()
    
    return render_to_response('app/orderList.html',{'deletable' : "true", "orders" : orders},context)
    
def order(request, order_id):
    context = RequestContext(request)
    order_form = OrderForm(instance=Order.objects.get(pk=order_id))  
    
    orderItems = OrderItem.objects.filter(order=Order.objects.get(pk=order_id))
    payments = Payment.objects.filter(order=Order.objects.get(pk=order_id))
    invoices = Invoice.objects.filter(order=Order.objects.get(pk=order_id))
    return render_to_response('app/order.html',{'orderForm': order_form, 'order_id': order_id, 'editable' : 'true', 'orderItems' : orderItems, 'payments' : payments, 'invoices' : invoices}, context)
    
def add_order(request):
    context = RequestContext(request)
    if request.method == 'POST':
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            order = order_form.save()
            order.save()
            
            return render_to_response('app/order.html',{"orderForm" : order_form},context)    
        else: 
            messages.error(request, order_form.errors)
    else:
        order_form = OrderForm()
        
        orderItems = OrderItem.objects.all()
        payments = Payment.objects.all()
        invoices = Invoice.objects.all()
    return render_to_response('app/orderAdd.html', {'orderForm': order_form, 'orderItems' : orderItems, 'payments' : payments, 'invoices' : invoices}, context)
    
    
def modify_order(request, order_id):
    context = RequestContext(request)
    orderFromDB = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=orderFromDB)
        if order_form.is_valid():
            order = order_form.save()
            order.save()
            
            orderItems = OrderItem.objects.filter(order=Order.objects.get(pk=order_id))
            payments = Payment.objects.filter(order=Order.objects.get(pk=order_id))
            invoices = Invoice.objects.filter(order=Order.objects.get(pk=order_id))
            return render_to_response('app/order.html', {'orderForm': order_form, 'orderItems' : orderItems, 'payments' : payments, 'invoices' : invoices, 'order_id': order_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, order_form.errors)
        
    order_form = OrderForm(instance=orderFromDB)
    return render_to_response('app/orderAdd.html', {'orderForm': order_form}, context)
            
def delete_order(request, order_id):
    context = RequestContext(request)
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        order.delete();
        
    orders = Order.objects.all()    
    return render_to_response('app/orderList.html',{"orders" : orders},context)
    

def list_priceListItem(request):
    context = RequestContext(request)
    priceListItems = PriceListItem.objects.all()
    
    return render_to_response('app/priceListItemList.html',{'deletable' : "true", "priceListItems" : priceListItems},context)
    
def priceListItem(request, priceListItem_id):
    context = RequestContext(request)
    priceListItem_form = PriceListItemForm(instance=PriceListItem.objects.get(pk=priceListItem_id))  
    
    return render_to_response('app/priceListItem.html',{'priceListItemForm': priceListItem_form, 'priceListItem_id': priceListItem_id, 'editable' : 'true'}, context)
    
def add_priceListItem(request):
    context = RequestContext(request)
    if request.method == 'POST':
        priceListItem_form = PriceListItemForm(data=request.POST)
        if priceListItem_form.is_valid():
            priceListItem = priceListItem_form.save()
            priceListItem.save()
            
            return render_to_response('app/priceListItem.html',{"priceListItemForm" : priceListItem_form},context)    
        else: 
            messages.error(request, priceListItem_form.errors)
    else:
        priceListItem_form = PriceListItemForm()
        
    return render_to_response('app/priceListItemAdd.html', {'priceListItemForm': priceListItem_form}, context)
    
    
def modify_priceListItem(request, priceListItem_id):
    context = RequestContext(request)
    priceListItemFromDB = PriceListItem.objects.get(pk=priceListItem_id)
    if request.method == 'POST':
        priceListItem_form = PriceListItemForm(request.POST, instance=priceListItemFromDB)
        if priceListItem_form.is_valid():
            priceListItem = priceListItem_form.save()
            priceListItem.save()
            
            return render_to_response('app/priceListItem.html', {'priceListItemForm': priceListItem_form, 'priceListItem_id': priceListItem_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, priceListItem_form.errors)
        
    priceListItem_form = PriceListItemForm(instance=priceListItemFromDB)
    return render_to_response('app/priceListItemAdd.html', {'priceListItemForm': priceListItem_form}, context)
            
def delete_priceListItem(request, priceListItem_id):
    context = RequestContext(request)
    priceListItem = PriceListItem.objects.get(pk=priceListItem_id)
    if request.method == 'POST':
        priceListItem.delete();
        
    priceListItems = PriceListItem.objects.all()    
    return render_to_response('app/priceListItemList.html',{"priceListItems" : priceListItems},context)
    

def list_payment(request):
    context = RequestContext(request)
    payments = Payment.objects.all()
    
    return render_to_response('app/paymentList.html',{'deletable' : "true", "payments" : payments},context)
    
def payment(request, payment_id):
    context = RequestContext(request)
    payment_form = PaymentForm(instance=Payment.objects.get(pk=payment_id))  
    
    return render_to_response('app/payment.html',{'paymentForm': payment_form, 'payment_id': payment_id, 'editable' : 'true'}, context)
    
def add_payment(request):
    context = RequestContext(request)
    if request.method == 'POST':
        payment_form = PaymentForm(data=request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            payment.save()
            
            return render_to_response('app/payment.html',{"paymentForm" : payment_form},context)    
        else: 
            messages.error(request, payment_form.errors)
    else:
        payment_form = PaymentForm()
        
    return render_to_response('app/paymentAdd.html', {'paymentForm': payment_form}, context)
    
    
def modify_payment(request, payment_id):
    context = RequestContext(request)
    paymentFromDB = Payment.objects.get(pk=payment_id)
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST, instance=paymentFromDB)
        if payment_form.is_valid():
            payment = payment_form.save()
            payment.save()
            
            return render_to_response('app/payment.html', {'paymentForm': payment_form, 'payment_id': payment_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, payment_form.errors)
        
    payment_form = PaymentForm(instance=paymentFromDB)
    return render_to_response('app/paymentAdd.html', {'paymentForm': payment_form}, context)
            
def delete_payment(request, payment_id):
    context = RequestContext(request)
    payment = Payment.objects.get(pk=payment_id)
    if request.method == 'POST':
        payment.delete();
        
    payments = Payment.objects.all()    
    return render_to_response('app/paymentList.html',{"payments" : payments},context)
    

def list_invoice(request):
    context = RequestContext(request)
    invoices = Invoice.objects.all()
    
    return render_to_response('app/invoiceList.html',{'deletable' : "true", "invoices" : invoices},context)
    
def invoice(request, invoice_id):
    context = RequestContext(request)
    invoice_form = InvoiceForm(instance=Invoice.objects.get(pk=invoice_id))  
    
    return render_to_response('app/invoice.html',{'invoiceForm': invoice_form, 'invoice_id': invoice_id, 'editable' : 'true'}, context)
    
def add_invoice(request):
    context = RequestContext(request)
    if request.method == 'POST':
        invoice_form = InvoiceForm(data=request.POST)
        if invoice_form.is_valid():
            invoice = invoice_form.save()
            invoice.save()
            
            return render_to_response('app/invoice.html',{"invoiceForm" : invoice_form},context)    
        else: 
            messages.error(request, invoice_form.errors)
    else:
        invoice_form = InvoiceForm()
        
    return render_to_response('app/invoiceAdd.html', {'invoiceForm': invoice_form}, context)
    
    
def modify_invoice(request, invoice_id):
    context = RequestContext(request)
    invoiceFromDB = Invoice.objects.get(pk=invoice_id)
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST, instance=invoiceFromDB)
        if invoice_form.is_valid():
            invoice = invoice_form.save()
            invoice.save()
            
            return render_to_response('app/invoice.html', {'invoiceForm': invoice_form, 'invoice_id': invoice_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, invoice_form.errors)
        
    invoice_form = InvoiceForm(instance=invoiceFromDB)
    return render_to_response('app/invoiceAdd.html', {'invoiceForm': invoice_form}, context)
            
def delete_invoice(request, invoice_id):
    context = RequestContext(request)
    invoice = Invoice.objects.get(pk=invoice_id)
    if request.method == 'POST':
        invoice.delete();
        
    invoices = Invoice.objects.all()    
    return render_to_response('app/invoiceList.html',{"invoices" : invoices},context)
    

def list_customer(request):
    context = RequestContext(request)
    customers = Customer.objects.all()
    
    return render_to_response('app/customerList.html',{'deletable' : "true", "customers" : customers},context)
    
def customer(request, customer_id):
    context = RequestContext(request)
    customer_form = CustomerForm(instance=Customer.objects.get(pk=customer_id))  
    
    orders = Order.objects.filter(customer=Customer.objects.get(pk=customer_id))
    return render_to_response('app/customer.html',{'customerForm': customer_form, 'customer_id': customer_id, 'editable' : 'true', 'orders' : orders}, context)
    
def add_customer(request):
    context = RequestContext(request)
    if request.method == 'POST':
        customer_form = CustomerForm(data=request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()
            customer.save()
            
            return render_to_response('app/customer.html',{"customerForm" : customer_form},context)    
        else: 
            messages.error(request, customer_form.errors)
    else:
        customer_form = CustomerForm()
        
        orders = Order.objects.all()
    return render_to_response('app/customerAdd.html', {'customerForm': customer_form, 'orders' : orders}, context)
    
    
def modify_customer(request, customer_id):
    context = RequestContext(request)
    customerFromDB = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customerFromDB)
        if customer_form.is_valid():
            customer = customer_form.save()
            customer.save()
            
            orders = Order.objects.filter(customer=Customer.objects.get(pk=customer_id))
            return render_to_response('app/customer.html', {'customerForm': customer_form, 'orders' : orders, 'customer_id': customer_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, customer_form.errors)
        
    customer_form = CustomerForm(instance=customerFromDB)
    return render_to_response('app/customerAdd.html', {'customerForm': customer_form}, context)
            
def delete_customer(request, customer_id):
    context = RequestContext(request)
    customer = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        customer.delete();
        
    customers = Customer.objects.all()    
    return render_to_response('app/customerList.html',{"customers" : customers},context)
    

def list_priceList(request):
    context = RequestContext(request)
    priceLists = PriceList.objects.all()
    
    return render_to_response('app/priceListList.html',{'deletable' : "true", "priceLists" : priceLists},context)
    
def priceList(request, priceList_id):
    context = RequestContext(request)
    priceList_form = PriceListForm(instance=PriceList.objects.get(pk=priceList_id))  
    
    priceListItems = PriceListItem.objects.filter(priceList=PriceList.objects.get(pk=priceList_id))
    return render_to_response('app/priceList.html',{'priceListForm': priceList_form, 'priceList_id': priceList_id, 'editable' : 'true', 'priceListItems' : priceListItems}, context)
    
def add_priceList(request):
    context = RequestContext(request)
    if request.method == 'POST':
        priceList_form = PriceListForm(data=request.POST)
        if priceList_form.is_valid():
            priceList = priceList_form.save()
            priceList.save()
            
            return render_to_response('app/priceList.html',{"priceListForm" : priceList_form},context)    
        else: 
            messages.error(request, priceList_form.errors)
    else:
        priceList_form = PriceListForm()
        
        priceListItems = PriceListItem.objects.all()
    return render_to_response('app/priceListAdd.html', {'priceListForm': priceList_form, 'priceListItems' : priceListItems}, context)
    
    
def modify_priceList(request, priceList_id):
    context = RequestContext(request)
    priceListFromDB = PriceList.objects.get(pk=priceList_id)
    if request.method == 'POST':
        priceList_form = PriceListForm(request.POST, instance=priceListFromDB)
        if priceList_form.is_valid():
            priceList = priceList_form.save()
            priceList.save()
            
            priceListItems = PriceListItem.objects.filter(priceList=PriceList.objects.get(pk=priceList_id))
            return render_to_response('app/priceList.html', {'priceListForm': priceList_form, 'priceListItems' : priceListItems, 'priceList_id': priceList_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, priceList_form.errors)
        
    priceList_form = PriceListForm(instance=priceListFromDB)
    return render_to_response('app/priceListAdd.html', {'priceListForm': priceList_form}, context)
            
def delete_priceList(request, priceList_id):
    context = RequestContext(request)
    priceList = PriceList.objects.get(pk=priceList_id)
    if request.method == 'POST':
        priceList.delete();
        
    priceLists = PriceList.objects.all()    
    return render_to_response('app/priceListList.html',{"priceLists" : priceLists},context)
    

def list_stock(request):
    context = RequestContext(request)
    stocks = Stock.objects.all()
    
    return render_to_response('app/stockList.html',{'deletable' : "true", "stocks" : stocks},context)
    
def stock(request, stock_id):
    context = RequestContext(request)
    stock_form = StockForm(instance=Stock.objects.get(pk=stock_id))  
    
    stockKeepingUnits = StockKeepingUnit.objects.filter(stock=Stock.objects.get(pk=stock_id))
    return render_to_response('app/stock.html',{'stockForm': stock_form, 'stock_id': stock_id, 'editable' : 'true', 'stockKeepingUnits' : stockKeepingUnits}, context)
    
def add_stock(request):
    context = RequestContext(request)
    if request.method == 'POST':
        stock_form = StockForm(data=request.POST)
        if stock_form.is_valid():
            stock = stock_form.save()
            stock.save()
            
            return render_to_response('app/stock.html',{"stockForm" : stock_form},context)    
        else: 
            messages.error(request, stock_form.errors)
    else:
        stock_form = StockForm()
        
        stockKeepingUnits = StockKeepingUnit.objects.all()
    return render_to_response('app/stockAdd.html', {'stockForm': stock_form, 'stockKeepingUnits' : stockKeepingUnits}, context)
    
    
def modify_stock(request, stock_id):
    context = RequestContext(request)
    stockFromDB = Stock.objects.get(pk=stock_id)
    if request.method == 'POST':
        stock_form = StockForm(request.POST, instance=stockFromDB)
        if stock_form.is_valid():
            stock = stock_form.save()
            stock.save()
            
            stockKeepingUnits = StockKeepingUnit.objects.filter(stock=Stock.objects.get(pk=stock_id))
            return render_to_response('app/stock.html', {'stockForm': stock_form, 'stockKeepingUnits' : stockKeepingUnits, 'stock_id': stock_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, stock_form.errors)
        
    stock_form = StockForm(instance=stockFromDB)
    return render_to_response('app/stockAdd.html', {'stockForm': stock_form}, context)
            
def delete_stock(request, stock_id):
    context = RequestContext(request)
    stock = Stock.objects.get(pk=stock_id)
    if request.method == 'POST':
        stock.delete();
        
    stocks = Stock.objects.all()    
    return render_to_response('app/stockList.html',{"stocks" : stocks},context)
    

def list_product(request):
    context = RequestContext(request)
    products = Product.objects.all()
    
    return render_to_response('app/productList.html',{'deletable' : "true", "products" : products},context)
    
def product(request, product_id):
    context = RequestContext(request)
    product_form = ProductForm(instance=Product.objects.get(pk=product_id))  
    
    priceListItems = PriceListItem.objects.filter(product=Product.objects.get(pk=product_id))
    orderItems = OrderItem.objects.filter(product=Product.objects.get(pk=product_id))
    return render_to_response('app/product.html',{'productForm': product_form, 'product_id': product_id, 'editable' : 'true', 'priceListItems' : priceListItems, 'orderItems' : orderItems}, context)
    
def add_product(request):
    context = RequestContext(request)
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        if product_form.is_valid():
            product = product_form.save()
            product.save()
            
            return render_to_response('app/product.html',{"productForm" : product_form},context)    
        else: 
            messages.error(request, product_form.errors)
    else:
        product_form = ProductForm()
        
        priceListItems = PriceListItem.objects.all()
        orderItems = OrderItem.objects.all()
    return render_to_response('app/productAdd.html', {'productForm': product_form, 'priceListItems' : priceListItems, 'orderItems' : orderItems}, context)
    
    
def modify_product(request, product_id):
    context = RequestContext(request)
    productFromDB = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=productFromDB)
        if product_form.is_valid():
            product = product_form.save()
            product.save()
            
            priceListItems = PriceListItem.objects.filter(product=Product.objects.get(pk=product_id))
            orderItems = OrderItem.objects.filter(product=Product.objects.get(pk=product_id))
            return render_to_response('app/product.html', {'productForm': product_form, 'priceListItems' : priceListItems, 'orderItems' : orderItems, 'product_id': product_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, product_form.errors)
        
    product_form = ProductForm(instance=productFromDB)
    return render_to_response('app/productAdd.html', {'productForm': product_form}, context)
            
def delete_product(request, product_id):
    context = RequestContext(request)
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete();
        
    products = Product.objects.all()    
    return render_to_response('app/productList.html',{"products" : products},context)
    

def list_category(request):
    context = RequestContext(request)
    categorys = Category.objects.all()
    
    return render_to_response('app/categoryList.html',{'deletable' : "true", "categorys" : categorys},context)
    
def category(request, category_id):
    context = RequestContext(request)
    category_form = CategoryForm(instance=Category.objects.get(pk=category_id))  
    
    products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    categorys = Category.objects.filter(category=Category.objects.get(pk=category_id))
    return render_to_response('app/category.html',{'categoryForm': category_form, 'category_id': category_id, 'editable' : 'true', 'products' : products, 'categorys' : categorys}, context)
    
def add_category(request):
    context = RequestContext(request)
    if request.method == 'POST':
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            category = category_form.save()
            category.save()
            
            return render_to_response('app/category.html',{"categoryForm" : category_form},context)    
        else: 
            messages.error(request, category_form.errors)
    else:
        category_form = CategoryForm()
        
        products = Product.objects.all()
        categorys = Category.objects.all()
    return render_to_response('app/categoryAdd.html', {'categoryForm': category_form, 'products' : products, 'categorys' : categorys}, context)
    
    
def modify_category(request, category_id):
    context = RequestContext(request)
    categoryFromDB = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=categoryFromDB)
        if category_form.is_valid():
            category = category_form.save()
            category.save()
            
            products = Product.objects.filter(category=Category.objects.get(pk=category_id))
            categorys = Category.objects.filter(category=Category.objects.get(pk=category_id))
            return render_to_response('app/category.html', {'categoryForm': category_form, 'products' : products, 'categorys' : categorys, 'category_id': category_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, category_form.errors)
        
    category_form = CategoryForm(instance=categoryFromDB)
    return render_to_response('app/categoryAdd.html', {'categoryForm': category_form}, context)
            
def delete_category(request, category_id):
    context = RequestContext(request)
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        category.delete();
        
    categorys = Category.objects.all()    
    return render_to_response('app/categoryList.html',{"categorys" : categorys},context)
    

def list_stockKeepingUnit(request):
    context = RequestContext(request)
    stockKeepingUnits = StockKeepingUnit.objects.all()
    
    return render_to_response('app/stockKeepingUnitList.html',{'deletable' : "true", "stockKeepingUnits" : stockKeepingUnits},context)
    
def stockKeepingUnit(request, stockKeepingUnit_id):
    context = RequestContext(request)
    stockKeepingUnit_form = StockKeepingUnitForm(instance=StockKeepingUnit.objects.get(pk=stockKeepingUnit_id))  
    
    products = Product.objects.filter(stockKeepingUnit=StockKeepingUnit.objects.get(pk=stockKeepingUnit_id))
    return render_to_response('app/stockKeepingUnit.html',{'stockKeepingUnitForm': stockKeepingUnit_form, 'stockKeepingUnit_id': stockKeepingUnit_id, 'editable' : 'true', 'products' : products}, context)
    
def add_stockKeepingUnit(request):
    context = RequestContext(request)
    if request.method == 'POST':
        stockKeepingUnit_form = StockKeepingUnitForm(data=request.POST)
        if stockKeepingUnit_form.is_valid():
            stockKeepingUnit = stockKeepingUnit_form.save()
            stockKeepingUnit.save()
            
            return render_to_response('app/stockKeepingUnit.html',{"stockKeepingUnitForm" : stockKeepingUnit_form},context)    
        else: 
            messages.error(request, stockKeepingUnit_form.errors)
    else:
        stockKeepingUnit_form = StockKeepingUnitForm()
        
        products = Product.objects.all()
    return render_to_response('app/stockKeepingUnitAdd.html', {'stockKeepingUnitForm': stockKeepingUnit_form, 'products' : products}, context)
    
    
def modify_stockKeepingUnit(request, stockKeepingUnit_id):
    context = RequestContext(request)
    stockKeepingUnitFromDB = StockKeepingUnit.objects.get(pk=stockKeepingUnit_id)
    if request.method == 'POST':
        stockKeepingUnit_form = StockKeepingUnitForm(request.POST, instance=stockKeepingUnitFromDB)
        if stockKeepingUnit_form.is_valid():
            stockKeepingUnit = stockKeepingUnit_form.save()
            stockKeepingUnit.save()
            
            products = Product.objects.filter(stockKeepingUnit=StockKeepingUnit.objects.get(pk=stockKeepingUnit_id))
            return render_to_response('app/stockKeepingUnit.html', {'stockKeepingUnitForm': stockKeepingUnit_form, 'products' : products, 'stockKeepingUnit_id': stockKeepingUnit_id, 'editable' : 'true'},context)
        else: 
            messages.error(request, stockKeepingUnit_form.errors)
        
    stockKeepingUnit_form = StockKeepingUnitForm(instance=stockKeepingUnitFromDB)
    return render_to_response('app/stockKeepingUnitAdd.html', {'stockKeepingUnitForm': stockKeepingUnit_form}, context)
            
def delete_stockKeepingUnit(request, stockKeepingUnit_id):
    context = RequestContext(request)
    stockKeepingUnit = StockKeepingUnit.objects.get(pk=stockKeepingUnit_id)
    if request.method == 'POST':
        stockKeepingUnit.delete();
        
    stockKeepingUnits = StockKeepingUnit.objects.all()    
    return render_to_response('app/stockKeepingUnitList.html',{"stockKeepingUnits" : stockKeepingUnits},context)
    
