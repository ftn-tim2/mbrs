from django.contrib import admin
from TODO_name.models import City
from TODO_name.models import Enterprise
from TODO_name.models import State
from TODO_name.models import Department
from TODO_name.models import Vendor
from TODO_name.models import OrderItem
from TODO_name.models import Order
from TODO_name.models import PriceListItem
from TODO_name.models import Payment
from TODO_name.models import Invoice
from TODO_name.models import Customer
from TODO_name.models import PriceList
from TODO_name.models import Stock
from TODO_name.models import Product
from TODO_name.models import Category
from TODO_name.models import StockKeepingUnit
# Handle the signal sent by user_login
from registration.signals import user_registered
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission


def user_registered_handler(sender, **kwargs):
    """signal intercept for user_registered"""
    request = kwargs['request']
    new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
    view_permissions = ['view_city', 'view_enterprise', 'view_state', 'view_department', 'view_vendor', 'view_orderitem', 'view_order', 'view_pricelistitem', 'view_payment', 'view_invoice', 'view_customer', 'view_pricelist', 'view_stock', 'view_product', 'view_category', 'view_stockkeepingunit', ]
    for v_perm in view_permissions:
        permission = Permission.objects.get(codename=v_perm)
        if permission:
            new_user.user_permissions.add(permission)

user_registered.connect(user_registered_handler)
admin.site.register(City)
admin.site.register(Enterprise)
admin.site.register(State)
admin.site.register(Department)
admin.site.register(Vendor)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(PriceListItem)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Customer)
admin.site.register(PriceList)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(StockKeepingUnit)
