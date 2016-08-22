from django import forms
from django.utils import timezone
from django.forms.widgets import TextInput, Textarea, Select, DateInput, NumberInput, CheckboxInput

from app.models import City, Enterprise, State, Department, Vendor, OrderItem, Order, PriceListItem, Payment, Invoice, Customer, PriceList, Stock, Product, Category, StockKeepingUnit, PAYMENTMETHOD, ORDERSTATUS

class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = (
    		'name',
    		'zipCode',
    		'state',
		)
		
		widgets = {
    		'name' : TextInput(attrs={'class':'form-control'}),
    		'zipCode' : TextInput(attrs={'class':'form-control'}),
    		'state' : Select(attrs={'class':'form-control'}, choices=State.objects.all()),
		}
	
class EnterpriseForm(forms.ModelForm):
	class Meta:
		model = Enterprise
		fields = (
    		'name',
    		'address',
    		'city',
		)
		
		widgets = {
    		'name' : TextInput(attrs={'class':'form-control'}),
    		'address' : TextInput(attrs={'class':'form-control'}),
    		'city' : Select(attrs={'class':'form-control'}, choices=City.objects.all()),
		}
	
class StateForm(forms.ModelForm):
	class Meta:
		model = State
		fields = (
    		'name',
		)
		
		widgets = {
    		'name' : Textarea(attrs={'class':'form-control', 'rows':'3'}),
		}
	
class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = (
    		'departmentName',
    		'address',
    		'enterprise',
    		'city',
		)
		
		widgets = {
    		'departmentName' : TextInput(attrs={'class':'form-control'}),
    		'address' : TextInput(attrs={'class':'form-control'}),
    		'enterprise' : Select(attrs={'class':'form-control'}, choices=Enterprise.objects.all()),
    		'city' : Select(attrs={'class':'form-control'}, choices=City.objects.all()),
		}
	
class VendorForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields = (
    		'name',
    		'address',
    		'city',
		)
		
		widgets = {
    		'name' : TextInput(attrs={'class':'form-control'}),
    		'address' : TextInput(attrs={'class':'form-control'}),
    		'city' : Select(attrs={'class':'form-control'}, choices=City.objects.all()),
		}
	
class OrderItemForm(forms.ModelForm):
	class Meta:
		model = OrderItem
		fields = (
    		'orderedQuantity',
    		'available',
    		'unitPrice',
    		'unitTax',
    		'value',
    		'order',
    		'product',
		)
		
		widgets = {
  			'orderedQuantity' : NumberInput(attrs={'class':'form-control'}),	
  			'available' : NumberInput(attrs={'class':'form-control'}),	
  			'unitPrice' : NumberInput(attrs={'class':'form-control'}),	
  			'unitTax' : NumberInput(attrs={'class':'form-control'}),	
  			'value' : NumberInput(attrs={'class':'form-control'}),	
    		'order' : Select(attrs={'class':'form-control'}, choices=Order.objects.all()),
    		'product' : Select(attrs={'class':'form-control'}, choices=Product.objects.all()),
		}
	
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = (
    		'orderNumber',
    		'shipmentAddress',
    		'orderDate',
    		
    		'orderTotal',
    		'orderStatus',
    		'city',
    		'customer',
		)
		
		widgets = {
  			'orderNumber' : NumberInput(attrs={'class':'form-control'}),	
    		'shipmentAddress' : TextInput(attrs={'class':'form-control'}),
  			'orderDate' : DateInput(attrs={'class':'form-control'}),
  			'orderTotal' : NumberInput(attrs={'class':'form-control'}),	
    		'orderStatus' : TextInput(attrs={'class':'form-control'}),
    		'city' : Select(attrs={'class':'form-control'}, choices=City.objects.all()),
    		'customer' : Select(attrs={'class':'form-control'}, choices=Customer.objects.all()),
		}
	
class PriceListItemForm(forms.ModelForm):
	class Meta:
		model = PriceListItem
		fields = (
    		'price',
    		'tax',
    		'product',
    		'priceList',
		)
		
		widgets = {
  			'price' : NumberInput(attrs={'class':'form-control'}),	
  			'tax' : NumberInput(attrs={'class':'form-control'}),	
    		'product' : Select(attrs={'class':'form-control'}, choices=Product.objects.all()),
    		'priceList' : Select(attrs={'class':'form-control'}, choices=PriceList.objects.all()),
		}
	
class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = (
    		'paymetMethod',
    		'amountReceived',
    		'canceled',
    		'dateReceived',
    		
    		'order',
		)
		
		widgets = {
    		'paymetMethod' : Select(attrs={'class':'form-control'}, choices=PAYMENTMETHOD),
  			'amountReceived' : NumberInput(attrs={'class':'form-control'}),	
  			'canceled' : CheckboxInput(attrs={'class':'form-control'}),	
  			'dateReceived' : DateInput(attrs={'class':'form-control'}),
    		'order' : Select(attrs={'class':'form-control'}, choices=Order.objects.all()),
		}
	
class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = (
    		'invoiceNumber',
    		'canceled',
    		'invoiceDate',
    		
    		'invoiceTotal',
    		'order',
		)
		
		widgets = {
    		'invoiceNumber' : TextInput(attrs={'class':'form-control'}),
  			'canceled' : CheckboxInput(attrs={'class':'form-control'}),	
  			'invoiceDate' : DateInput(attrs={'class':'form-control'}),
    		'invoiceTotal' : TextInput(attrs={'class':'form-control'}),
    		'order' : Select(attrs={'class':'form-control'}, choices=Order.objects.all()),
		}
	
class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = (
    		'name',
    		'address',
    		'city',
		)
		
		widgets = {
    		'name' : TextInput(attrs={'class':'form-control'}),
    		'address' : TextInput(attrs={'class':'form-control'}),
    		'city' : Select(attrs={'class':'form-control'}, choices=City.objects.all()),
		}
	
class PriceListForm(forms.ModelForm):
	class Meta:
		model = PriceList
		fields = (
    		'listNumber',
    		'activeFromDate',
    		
		)
		
		widgets = {
  			'listNumber' : NumberInput(attrs={'class':'form-control'}),	
  			'activeFromDate' : DateInput(attrs={'class':'form-control'}),
		}
	
class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = (
    		'stockName',
    		'desription',
    		'department',
		)
		
		widgets = {
    		'stockName' : TextInput(attrs={'class':'form-control'}),
    		'desription' : Textarea(attrs={'class':'form-control', 'rows':'3'}),
    		'department' : Select(attrs={'class':'form-control'}, choices=Department.objects.all()),
		}
	
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = (
    		'productName',
    		'description',
    		'stockKeepingUnit',
    		'category',
    		'vendor',
		)
		
		widgets = {
    		'productName' : TextInput(attrs={'class':'form-control'}),
    		'description' : Textarea(attrs={'class':'form-control', 'rows':'3'}),
    		'stockKeepingUnit' : Select(attrs={'class':'form-control'}, choices=StockKeepingUnit.objects.all()),
    		'category' : Select(attrs={'class':'form-control'}, choices=Category.objects.all()),
    		'vendor' : Select(attrs={'class':'form-control'}, choices=Vendor.objects.all()),
		}
	
class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = (
    		'cactegoryName',
    		'description',
    		'subcategory',
		)
		
		widgets = {
    		'cactegoryName' : TextInput(attrs={'class':'form-control'}),
    		'description' : TextInput(attrs={'class':'form-control'}),
			'subcategory' : Select(attrs={'class':'form-control'}, choices=Category.objects.all()),
		}
	
class StockKeepingUnitForm(forms.ModelForm):
	class Meta:
		model = StockKeepingUnit
		fields = (
    		'available',
    		'reserved',
    		'stock',
		)
		
		widgets = {
  			'available' : NumberInput(attrs={'class':'form-control'}),	
  			'reserved' : NumberInput(attrs={'class':'form-control'}),	
    		'stock' : Select(attrs={'class':'form-control'}, choices=Stock.objects.all()),
		}
	


