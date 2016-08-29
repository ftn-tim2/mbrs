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
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
import test


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['enterprise', 'name', 'zipCode', 'department', 'vendor', 'order', 'customer']


@permission_required('TODO_name.view_city')
@login_required
def city_list(request, template_name='TODO_name/city_list.html'):
    city = City.objects.all()
    data = {'object_list': city}
    return render(request, template_name, data)


@permission_required('TODO_name.add_city')
@login_required
def city_create(request, template_name='TODO_name/city_form.html'):
    form = CityForm(request.POST or None)
    if form.is_valid():
        city = form.save(commit=False)
        city.user = request.user
        city.save()
        return redirect('TODO_name:city_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_city')
@login_required
def city_update(request, pk, template_name='TODO_name/city_form.html'):
    city = get_object_or_404(City, pk=pk)
    form = CityForm(request.POST or None, instance=city)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:city_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_city')
@login_required
def city_delete(request, pk, template_name='TODO_name/city_confirm_delete.html'):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('TODO_name:city_list')
    return render(request, template_name, {'object': city, 'form_type': 'Delete'})


class EnterpriseForm(ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name', 'address', 'department']


@permission_required('TODO_name.view_enterprise')
@login_required
def enterprise_list(request, template_name='TODO_name/enterprise_list.html'):
    enterprise = Enterprise.objects.all()
    data = {'object_list': enterprise}
    return render(request, template_name, data)


@permission_required('TODO_name.add_enterprise')
@login_required
def enterprise_create(request, template_name='TODO_name/enterprise_form.html'):
    form = EnterpriseForm(request.POST or None)
    if form.is_valid():
        enterprise = form.save(commit=False)
        enterprise.user = request.user
        enterprise.save()
        return redirect('TODO_name:enterprise_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_enterprise')
@login_required
def enterprise_update(request, pk, template_name='TODO_name/enterprise_form.html'):
    enterprise = get_object_or_404(Enterprise, pk=pk)
    form = EnterpriseForm(request.POST or None, instance=enterprise)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:enterprise_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_enterprise')
@login_required
def enterprise_delete(request, pk, template_name='TODO_name/enterprise_confirm_delete.html'):
    enterprise = get_object_or_404(Enterprise, pk=pk)
    if request.method == 'POST':
        enterprise.delete()
        return redirect('TODO_name:enterprise_list')
    return render(request, template_name, {'object': enterprise, 'form_type': 'Delete'})


class StateForm(ModelForm):
    class Meta:
        model = State
        fields = ['city', 'name']


@permission_required('TODO_name.view_state')
@login_required
def state_list(request, template_name='TODO_name/state_list.html'):
    state = State.objects.all()
    data = {'object_list': state}
    return render(request, template_name, data)


@permission_required('TODO_name.add_state')
@login_required
def state_create(request, template_name='TODO_name/state_form.html'):
    form = StateForm(request.POST or None)
    if form.is_valid():
        state = form.save(commit=False)
        state.user = request.user
        state.save()
        return redirect('TODO_name:state_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_state')
@login_required
def state_update(request, pk, template_name='TODO_name/state_form.html'):
    state = get_object_or_404(State, pk=pk)
    form = StateForm(request.POST or None, instance=state)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:state_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_state')
@login_required
def state_delete(request, pk, template_name='TODO_name/state_confirm_delete.html'):
    state = get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        state.delete()
        return redirect('TODO_name:state_list')
    return render(request, template_name, {'object': state, 'form_type': 'Delete'})


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['departmentName', 'address', 'stock']


@permission_required('TODO_name.view_department')
@login_required
def department_list(request, template_name='TODO_name/department_list.html'):
    department = Department.objects.all()
    data = {'object_list': department}
    return render(request, template_name, data)


@permission_required('TODO_name.add_department')
@login_required
def department_create(request, template_name='TODO_name/department_form.html'):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        department = form.save(commit=False)
        department.user = request.user
        department.save()
        return redirect('TODO_name:department_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_department')
@login_required
def department_update(request, pk, template_name='TODO_name/department_form.html'):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:department_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_department')
@login_required
def department_delete(request, pk, template_name='TODO_name/department_confirm_delete.html'):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('TODO_name:department_list')
    return render(request, template_name, {'object': department, 'form_type': 'Delete'})


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['product', 'name', 'address']


@permission_required('TODO_name.view_vendor')
@login_required
def vendor_list(request, template_name='TODO_name/vendor_list.html'):
    vendor = Vendor.objects.all()
    data = {'object_list': vendor}
    return render(request, template_name, data)


@permission_required('TODO_name.add_vendor')
@login_required
def vendor_create(request, template_name='TODO_name/vendor_form.html'):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        vendor = form.save(commit=False)
        vendor.user = request.user
        vendor.save()
        return redirect('TODO_name:vendor_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_vendor')
@login_required
def vendor_update(request, pk, template_name='TODO_name/vendor_form.html'):
    vendor = get_object_or_404(Vendor, pk=pk)
    form = VendorForm(request.POST or None, instance=vendor)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:vendor_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_vendor')
@login_required
def vendor_delete(request, pk, template_name='TODO_name/vendor_confirm_delete.html'):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('TODO_name:vendor_list')
    return render(request, template_name, {'object': vendor, 'form_type': 'Delete'})


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['orderedQuantity', 'available', 'unitPrice', 'unitTax', 'value']


@permission_required('TODO_name.view_orderitem')
@login_required
def orderitem_list(request, template_name='TODO_name/orderitem_list.html'):
    orderitem = OrderItem.objects.all()
    data = {'object_list': orderitem}
    return render(request, template_name, data)


@permission_required('TODO_name.add_orderitem')
@login_required
def orderitem_create(request, template_name='TODO_name/orderitem_form.html'):
    form = OrderItemForm(request.POST or None)
    if form.is_valid():
        orderitem = form.save(commit=False)
        orderitem.user = request.user
        orderitem.save()
        return redirect('TODO_name:orderitem_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_orderitem')
@login_required
def orderitem_update(request, pk, template_name='TODO_name/orderitem_form.html'):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    form = OrderItemForm(request.POST or None, instance=orderitem)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:orderitem_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_orderitem')
@login_required
def orderitem_delete(request, pk, template_name='TODO_name/orderitem_confirm_delete.html'):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        orderitem.delete()
        return redirect('TODO_name:orderitem_list')
    return render(request, template_name, {'object': orderitem, 'form_type': 'Delete'})


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['orderItem', 'payment', 'invoice', 'orderNumber', 'orderDate', 'shipmentAddress', 'orderTotal', 'orderStatus']


@permission_required('TODO_name.view_order')
@login_required
def order_list(request, template_name='TODO_name/order_list.html'):
    order = Order.objects.all()
    data = {'object_list': order}
    return render(request, template_name, data)


@permission_required('TODO_name.add_order')
@login_required
def order_create(request, template_name='TODO_name/order_form.html'):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.user = request.user
        order.save()
        return redirect('TODO_name:order_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_order')
@login_required
def order_update(request, pk, template_name='TODO_name/order_form.html'):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:order_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_order')
@login_required
def order_delete(request, pk, template_name='TODO_name/order_confirm_delete.html'):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('TODO_name:order_list')
    return render(request, template_name, {'object': order, 'form_type': 'Delete'})


class PriceListItemForm(ModelForm):
    class Meta:
        model = PriceListItem
        fields = ['price', 'tax']


@permission_required('TODO_name.view_pricelistitem')
@login_required
def pricelistitem_list(request, template_name='TODO_name/pricelistitem_list.html'):
    pricelistitem = PriceListItem.objects.all()
    data = {'object_list': pricelistitem}
    return render(request, template_name, data)


@permission_required('TODO_name.add_pricelistitem')
@login_required
def pricelistitem_create(request, template_name='TODO_name/pricelistitem_form.html'):
    form = PriceListItemForm(request.POST or None)
    if form.is_valid():
        pricelistitem = form.save(commit=False)
        pricelistitem.user = request.user
        pricelistitem.save()
        return redirect('TODO_name:pricelistitem_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_pricelistitem')
@login_required
def pricelistitem_update(request, pk, template_name='TODO_name/pricelistitem_form.html'):
    pricelistitem = get_object_or_404(PriceListItem, pk=pk)
    form = PriceListItemForm(request.POST or None, instance=pricelistitem)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:pricelistitem_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_pricelistitem')
@login_required
def pricelistitem_delete(request, pk, template_name='TODO_name/pricelistitem_confirm_delete.html'):
    pricelistitem = get_object_or_404(PriceListItem, pk=pk)
    if request.method == 'POST':
        pricelistitem.delete()
        return redirect('TODO_name:pricelistitem_list')
    return render(request, template_name, {'object': pricelistitem, 'form_type': 'Delete'})


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['paymetMethod', 'dateReceived', 'amountReceived', 'canceled']


@permission_required('TODO_name.view_payment')
@login_required
def payment_list(request, template_name='TODO_name/payment_list.html'):
    payment = Payment.objects.all()
    data = {'object_list': payment}
    return render(request, template_name, data)


@permission_required('TODO_name.add_payment')
@login_required
def payment_create(request, template_name='TODO_name/payment_form.html'):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        payment = form.save(commit=False)
        payment.user = request.user
        payment.save()
        return redirect('TODO_name:payment_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_payment')
@login_required
def payment_update(request, pk, template_name='TODO_name/payment_form.html'):
    payment = get_object_or_404(Payment, pk=pk)
    form = PaymentForm(request.POST or None, instance=payment)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:payment_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_payment')
@login_required
def payment_delete(request, pk, template_name='TODO_name/payment_confirm_delete.html'):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('TODO_name:payment_list')
    return render(request, template_name, {'object': payment, 'form_type': 'Delete'})


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoiceNumber', 'invoiceDate', 'invoiceTotal', 'canceled']


@permission_required('TODO_name.view_invoice')
@login_required
def invoice_list(request, template_name='TODO_name/invoice_list.html'):
    invoice = Invoice.objects.all()
    data = {'object_list': invoice}
    return render(request, template_name, data)


@permission_required('TODO_name.add_invoice')
@login_required
def invoice_create(request, template_name='TODO_name/invoice_form.html'):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        invoice = form.save(commit=False)
        invoice.user = request.user
        invoice.save()
        return redirect('TODO_name:invoice_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_invoice')
@login_required
def invoice_update(request, pk, template_name='TODO_name/invoice_form.html'):
    invoice = get_object_or_404(Invoice, pk=pk)
    form = InvoiceForm(request.POST or None, instance=invoice)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:invoice_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_invoice')
@login_required
def invoice_delete(request, pk, template_name='TODO_name/invoice_confirm_delete.html'):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('TODO_name:invoice_list')
    return render(request, template_name, {'object': invoice, 'form_type': 'Delete'})


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'order']


@permission_required('TODO_name.view_customer')
@login_required
def customer_list(request, template_name='TODO_name/customer_list.html'):
    customer = Customer.objects.all()
    data = {'object_list': customer}
    return render(request, template_name, data)


@permission_required('TODO_name.add_customer')
@login_required
def customer_create(request, template_name='TODO_name/customer_form.html'):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        customer = form.save(commit=False)
        customer.user = request.user
        customer.save()
        return redirect('TODO_name:customer_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_customer')
@login_required
def customer_update(request, pk, template_name='TODO_name/customer_form.html'):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:customer_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_customer')
@login_required
def customer_delete(request, pk, template_name='TODO_name/customer_confirm_delete.html'):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('TODO_name:customer_list')
    return render(request, template_name, {'object': customer, 'form_type': 'Delete'})


class PriceListForm(ModelForm):
    class Meta:
        model = PriceList
        fields = ['priceListItem', 'listNumber', 'activeFromDate']


@permission_required('TODO_name.view_pricelist')
@login_required
def pricelist_list(request, template_name='TODO_name/pricelist_list.html'):
    pricelist = PriceList.objects.all()
    data = {'object_list': pricelist}
    return render(request, template_name, data)


@permission_required('TODO_name.add_pricelist')
@login_required
def pricelist_create(request, template_name='TODO_name/pricelist_form.html'):
    form = PriceListForm(request.POST or None)
    if form.is_valid():
        pricelist = form.save(commit=False)
        pricelist.user = request.user
        pricelist.save()
        return redirect('TODO_name:pricelist_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_pricelist')
@login_required
def pricelist_update(request, pk, template_name='TODO_name/pricelist_form.html'):
    pricelist = get_object_or_404(PriceList, pk=pk)
    form = PriceListForm(request.POST or None, instance=pricelist)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:pricelist_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_pricelist')
@login_required
def pricelist_delete(request, pk, template_name='TODO_name/pricelist_confirm_delete.html'):
    pricelist = get_object_or_404(PriceList, pk=pk)
    if request.method == 'POST':
        pricelist.delete()
        return redirect('TODO_name:pricelist_list')
    return render(request, template_name, {'object': pricelist, 'form_type': 'Delete'})


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['stockKeepingUnit', 'stockName', 'desription']


@permission_required('TODO_name.view_stock')
@login_required
def stock_list(request, template_name='TODO_name/stock_list.html'):
    stock = Stock.objects.all()
    data = {'object_list': stock}
    return render(request, template_name, data)


@permission_required('TODO_name.add_stock')
@login_required
def stock_create(request, template_name='TODO_name/stock_form.html'):
    form = StockForm(request.POST or None)
    if form.is_valid():
        stock = form.save(commit=False)
        stock.user = request.user
        stock.save()
        return redirect('TODO_name:stock_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_stock')
@login_required
def stock_update(request, pk, template_name='TODO_name/stock_form.html'):
    stock = get_object_or_404(Stock, pk=pk)
    form = StockForm(request.POST or None, instance=stock)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:stock_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_stock')
@login_required
def stock_delete(request, pk, template_name='TODO_name/stock_confirm_delete.html'):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('TODO_name:stock_list')
    return render(request, template_name, {'object': stock, 'form_type': 'Delete'})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['priceListItem', 'orderItem', 'productName', 'description']


@permission_required('TODO_name.view_product')
@login_required
def product_list(request, template_name='TODO_name/product_list.html'):
    product = Product.objects.all()
    data = {'object_list': product}
    return render(request, template_name, data)


@permission_required('TODO_name.add_product')
@login_required
def product_create(request, template_name='TODO_name/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('TODO_name:product_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_product')
@login_required
def product_update(request, pk, template_name='TODO_name/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:product_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_product')
@login_required
def product_delete(request, pk, template_name='TODO_name/product_confirm_delete.html'):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('TODO_name:product_list')
    return render(request, template_name, {'object': product, 'form_type': 'Delete'})


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['product', 'category', 'categoryName', 'description']


@permission_required('TODO_name.view_category')
@login_required
def category_list(request, template_name='TODO_name/category_list.html'):
    category = Category.objects.all()
    data = {'object_list': category}
    return render(request, template_name, data)


@permission_required('TODO_name.add_category')
@login_required
def category_create(request, template_name='TODO_name/category_form.html'):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('TODO_name:category_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_category')
@login_required
def category_update(request, pk, template_name='TODO_name/category_form.html'):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:category_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_category')
@login_required
def category_delete(request, pk, template_name='TODO_name/category_confirm_delete.html'):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('TODO_name:category_list')
    return render(request, template_name, {'object': category, 'form_type': 'Delete'})


class StockKeepingUnitForm(ModelForm):
    class Meta:
        model = StockKeepingUnit
        fields = ['product', 'available', 'reserved']


@permission_required('TODO_name.view_stockkeepingunit')
@login_required
def stockkeepingunit_list(request, template_name='TODO_name/stockkeepingunit_list.html'):
    stockkeepingunit = StockKeepingUnit.objects.all()
    data = {'object_list': stockkeepingunit}
    return render(request, template_name, data)


@permission_required('TODO_name.add_stockkeepingunit')
@login_required
def stockkeepingunit_create(request, template_name='TODO_name/stockkeepingunit_form.html'):
    form = StockKeepingUnitForm(request.POST or None)
    if form.is_valid():
        stockkeepingunit = form.save(commit=False)
        stockkeepingunit.user = request.user
        stockkeepingunit.save()
        return redirect('TODO_name:stockkeepingunit_list')
    return render(request, template_name, {'form': form, 'form_type': 'Create'})


@permission_required('TODO_name.change_stockkeepingunit')
@login_required
def stockkeepingunit_update(request, pk, template_name='TODO_name/stockkeepingunit_form.html'):
    stockkeepingunit = get_object_or_404(StockKeepingUnit, pk=pk)
    form = StockKeepingUnitForm(request.POST or None, instance=stockkeepingunit)
    if form.is_valid():
        form.save()
        return redirect('TODO_name:stockkeepingunit_list')
    return render(request, template_name, {'form': form, 'form_type': 'Update'})


@permission_required('TODO_name.delete_stockkeepingunit')
@login_required
def stockkeepingunit_delete(request, pk, template_name='TODO_name/stockkeepingunit_confirm_delete.html'):
    stockkeepingunit = get_object_or_404(StockKeepingUnit, pk=pk)
    if request.method == 'POST':
        stockkeepingunit.delete()
        return redirect('TODO_name:stockkeepingunit_list')
    return render(request, template_name, {'object': stockkeepingunit, 'form_type': 'Delete'})
