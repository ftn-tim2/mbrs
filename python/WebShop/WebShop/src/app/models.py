import datetime

from django.db import models
from django.utils import timezone

PAYMENTMETHOD = (
    ('0', 'cash'),
    ('1', 'creditCard'),
    ('2', 'payPal'),
) 
ORDERSTATUS = (
    ('0', 'ordering'),
    ('1', 'finished'),
    ('2', 'canceled'),
    ('3', 'shipped'),
) 

class State(models.Model):
    name = models.CharField(max_length= 25, default ="")
    def __str__(self):
        return 'State: ' + 'name= ' + self.name.__str__() 
        
class PriceList(models.Model):
    listNumber = models.IntegerField(default=0)
    activeFromDate = models.DateField(default=timezone.now)
    def __str__(self):
        return 'PriceList: ' + 'listNumber= ' + self.listNumber.__str__() + ', ' + 'activeFromDate= ' + self.activeFromDate.__str__() 
        
class Category(models.Model):
    cactegoryName = models.CharField(max_length= 25, default ="")
    description = models.CharField(max_length= 150, default ="")
    subcategory = models.ForeignKey('self', null = False)
    def __str__(self):
        return 'Category: ' + 'cactegoryName= ' + self.cactegoryName.__str__() + ', ' + 'description= ' + self.description.__str__() 
        
class City(models.Model):
    name = models.CharField(max_length= 30, default ="")
    zipCode = models.CharField(max_length= 12, default ="")
    state = models.ForeignKey(State, null = False)
    def __str__(self):
        return 'City: ' + 'name= ' + self.name.__str__() + ', ' + 'zipCode= ' + self.zipCode.__str__() 
        
class Vendor(models.Model):
    name = models.CharField(max_length= 30, default ="")
    address = models.CharField(max_length= 150, default ="")
    city = models.ForeignKey(City, null = False)
    def __str__(self):
        return 'Vendor: ' + 'name= ' + self.name.__str__() + ', ' + 'address= ' + self.address.__str__() 
        
class Customer(models.Model):
    name = models.CharField(max_length= 31, default ="")
    address = models.CharField(max_length= 51, default ="")
    city = models.ForeignKey(City, null = False)
    def __str__(self):
        return 'Customer: ' + 'name= ' + self.name.__str__() + ', ' + 'address= ' + self.address.__str__() 
        
class Enterprise(models.Model):
    name = models.CharField(max_length= 50, default ="")
    address = models.CharField(max_length= 150, default ="")
    city = models.ForeignKey(City, null = False)
    def __str__(self):
        return 'Enterprise: ' + 'name= ' + self.name.__str__() + ', ' + 'address= ' + self.address.__str__() 
        
class Order(models.Model):
    orderDate = models.DateField(default=timezone.now)
    orderTotal = models.FloatField(max_length= 5, default=0)
    orderStatus = models.CharField(max_length= 24, default ="")
    orderNumber = models.IntegerField(default=0)
    shipmentAddress = models.CharField(max_length= 51, default ="")
    city = models.ForeignKey(City, null = False)
    customer = models.ForeignKey(Customer, null = False)
    def __str__(self):
        return 'Order: ' + 'orderDate= ' + self.orderDate.__str__() + ', ' + 'orderTotal= ' + self.orderTotal.__str__() + ', ' + 'orderStatus= ' + self.orderStatus.__str__() + ', ' + 'orderNumber= ' + self.orderNumber.__str__() + ', ' + 'shipmentAddress= ' + self.shipmentAddress.__str__() 
        
class Payment(models.Model):
    dateReceived = models.DateField(default=timezone.now)
    paymetMethod = models.CharField(choices=PAYMENTMETHOD, max_length= 50)
    amountReceived = models.FloatField(max_length= 9, default=0)
    canceled = models.BooleanField(default = False)
    order = models.ForeignKey(Order, null = False)
    def __str__(self):
        return 'Payment: ' + 'dateReceived= ' + self.dateReceived.__str__() + ', ' + 'paymetMethod= ' + self.paymetMethod.__str__() + ', ' + 'amountReceived= ' + self.amountReceived.__str__() + ', ' + 'canceled= ' + self.canceled.__str__() 
        
class Department(models.Model):
    departmentName = models.CharField(max_length= 20, default ="")
    address = models.CharField(max_length= 155, default ="")
    enterprise = models.ForeignKey(Enterprise, null = False)
    city = models.ForeignKey(City, null = False)
    def __str__(self):
        return 'Department: ' + 'departmentName= ' + self.departmentName.__str__() + ', ' + 'address= ' + self.address.__str__() 
        
class Invoice(models.Model):
    invoiceDate = models.DateField(default=timezone.now)
    invoiceTotal = models.CharField(max_length= 21, default ="")
    invoiceNumber = models.CharField(max_length= 21, default ="")
    canceled = models.BooleanField(default = False)
    order = models.ForeignKey(Order, null = False)
    def __str__(self):
        return 'Invoice: ' + 'invoiceDate= ' + self.invoiceDate.__str__() + ', ' + 'invoiceTotal= ' + self.invoiceTotal.__str__() + ', ' + 'invoiceNumber= ' + self.invoiceNumber.__str__() + ', ' + 'canceled= ' + self.canceled.__str__() 
        
class Stock(models.Model):
    stockName = models.CharField(max_length= 20, default ="")
    desription = models.CharField(max_length= 255, default ="")
    department = models.ForeignKey(Department, null = False)
    def __str__(self):
        return 'Stock: ' + 'stockName= ' + self.stockName.__str__() + ', ' + 'desription= ' + self.desription.__str__() 
        
class StockKeepingUnit(models.Model):
    available = models.FloatField(max_length= 0, default=0)
    reserved = models.FloatField(max_length= 5, default=0)
    stock = models.ForeignKey(Stock, null = False)
    def __str__(self):
        return 'StockKeepingUnit: ' + 'available= ' + self.available.__str__() + ', ' + 'reserved= ' + self.reserved.__str__() 
        
class Product(models.Model):
    productName = models.CharField(max_length= 25, default ="")
    description = models.CharField(max_length= 255, default ="")
    stockKeepingUnit = models.ForeignKey(StockKeepingUnit, null = False)
    category = models.ForeignKey(Category, null = False)
    vendor = models.ForeignKey(Vendor, null = False)
    def __str__(self):
        return 'Product: ' + 'productName= ' + self.productName.__str__() + ', ' + 'description= ' + self.description.__str__() 
        
class OrderItem(models.Model):
    value = models.FloatField(max_length= 10, default=0)
    orderedQuantity = models.FloatField(max_length= 3, default=0)
    available = models.FloatField(max_length= 4, default=0)
    unitPrice = models.FloatField(max_length= 8, default=0)
    unitTax = models.FloatField(max_length= 7, default=0)
    order = models.ForeignKey(Order, null = False)
    product = models.ForeignKey(Product, null = False)
    def __str__(self):
        return 'OrderItem: ' + 'value= ' + self.value.__str__() + ', ' + 'orderedQuantity= ' + self.orderedQuantity.__str__() + ', ' + 'available= ' + self.available.__str__() + ', ' + 'unitPrice= ' + self.unitPrice.__str__() + ', ' + 'unitTax= ' + self.unitTax.__str__() 
        
class PriceListItem(models.Model):
    price = models.FloatField(max_length= 5, default=0)
    tax = models.FloatField(max_length= 5, default=0)
    product = models.ForeignKey(Product, null = False)
    priceList = models.ForeignKey(PriceList, null = False)
    def __str__(self):
        return 'PriceListItem: ' + 'price= ' + self.price.__str__() + ', ' + 'tax= ' + self.tax.__str__() 
        

