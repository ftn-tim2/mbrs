from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class City(models.Model):
    state = models.ForeignKey(to='State')
    name = models.CharField(max_length=30, null=False)
    zipCode = models.CharField(max_length=12, null=False)

    class Meta:
        permissions = (
            ("view_city", "Can view the City"),
        )

    def __str__(self):
        return str(self.state)

    def get_absolute_url(self):
        return reverse('TODO_name:city_edit', kwargs={'pk': self.pk})


class Enterprise(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.ForeignKey(to='City')

    class Meta:
        permissions = (
            ("view_enterprise", "Can view the Enterprise"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:enterprise_edit', kwargs={'pk': self.pk})


class State(models.Model):
    name = models.CharField(max_length=25, null=False)

    class Meta:
        permissions = (
            ("view_state", "Can view the State"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:state_edit', kwargs={'pk': self.pk})


class Department(models.Model):
    departmentName = models.CharField(max_length=20, editable=True, null=False)
    address = models.CharField(max_length=155, null=False)
    enterprise = models.ForeignKey(to='Enterprise')
    city = models.ForeignKey(to='City')

    class Meta:
        permissions = (
            ("view_department", "Can view the Department"),
        )

    def __str__(self):
        return str(self.departmentName)

    def get_absolute_url(self):
        return reverse('TODO_name:department_edit', kwargs={'pk': self.pk})


class Vendor(models.Model):
    name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.ForeignKey(to='City')

    class Meta:
        permissions = (
            ("view_vendor", "Can view the Vendor"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:vendor_edit', kwargs={'pk': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(to='Order')
    product = models.ForeignKey(to='Product')
    orderedQuantity = models.DecimalField(decimal_places=2, null=False, max_digits=15)
    available = models.DecimalField(decimal_places=2, null=True, max_digits=15)
    unitPrice = models.DecimalField(decimal_places=2, null=False, max_digits=15)
    unitTax = models.DecimalField(decimal_places=2, null=False, max_digits=15)
    value = models.DecimalField(decimal_places=2, null=False, max_digits=10)

    class Meta:
        permissions = (
            ("view_orderitem", "Can view the OrderItem"),
        )

    def __str__(self):
        return str(self.order)

    def get_absolute_url(self):
        return reverse('TODO_name:orderitem_edit', kwargs={'pk': self.pk})


class Order(models.Model):
    orderNumber = models.IntegerField(null=False)
    orderDate = models.DateTimeField(null=False)
    shipmentAddress = models.TextField(max_length=200, null=False)
    orderTotal = models.IntegerField(null=False)
    orderStatus = models.CharField(max_length=30, null=False, choices=(("ordering","ORDERING"),("finished","FINISHED"),("canceled","CANCELED"),("shipped","SHIPPED")))
    city = models.ForeignKey(to='City')
    customer = models.ForeignKey(to='Customer')

    class Meta:
        permissions = (
            ("view_order", "Can view the Order"),
        )

    def __str__(self):
        return str(self.orderNumber)

    def get_absolute_url(self):
        return reverse('TODO_name:order_edit', kwargs={'pk': self.pk})


class PriceListItem(models.Model):
    product = models.ForeignKey(to='Product')
    priceList = models.ForeignKey(to='PriceList')
    price = models.DecimalField(decimal_places=2, null=False, max_digits=10)
    tax = models.DecimalField(decimal_places=2, null=False, max_digits=10)

    class Meta:
        permissions = (
            ("view_pricelistitem", "Can view the PriceListItem"),
        )

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('TODO_name:pricelistitem_edit', kwargs={'pk': self.pk})


class Payment(models.Model):
    order = models.ForeignKey(to='Order')
    paymetMethod = models.CharField(max_length=50, choices=(("cash","CASH"),("creditCard","CREDITCARD"),("payPal","PAYPAL")))
    dateReceived = models.DateTimeField(null=False)
    amountReceived = models.DecimalField(max_length=9, decimal_places=2, null=False, max_digits=10)
    canceled = models.BooleanField(null=False)

    class Meta:
        permissions = (
            ("view_payment", "Can view the Payment"),
        )

    def __str__(self):
        return str(self.order)

    def get_absolute_url(self):
        return reverse('TODO_name:payment_edit', kwargs={'pk': self.pk})


class Invoice(models.Model):
    order = models.ForeignKey(to='Order')
    invoiceNumber = models.IntegerField(null=False)
    invoiceDate = models.DateTimeField()
    invoiceTotal = models.TextField(max_length=300, null=True)
    canceled = models.BooleanField()

    class Meta:
        permissions = (
            ("view_invoice", "Can view the Invoice"),
        )

    def __str__(self):
        return str(self.order)

    def get_absolute_url(self):
        return reverse('TODO_name:invoice_edit', kwargs={'pk': self.pk})


class Customer(models.Model):
    name = models.CharField(max_length=31, null=False)
    address = models.CharField(max_length=51, null=False)
    city = models.ForeignKey(to='City')

    class Meta:
        permissions = (
            ("view_customer", "Can view the Customer"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:customer_edit', kwargs={'pk': self.pk})


class PriceList(models.Model):
    listNumber = models.IntegerField(null=False)
    activeFromDate = models.DateTimeField(null=False)

    class Meta:
        permissions = (
            ("view_pricelist", "Can view the PriceList"),
        )

    def __str__(self):
        return str(self.listNumber)

    def get_absolute_url(self):
        return reverse('TODO_name:pricelist_edit', kwargs={'pk': self.pk})


class Stock(models.Model):
    department = models.ForeignKey(to='Department')
    stockName = models.CharField(max_length=20, null=False)
    desription = models.TextField(max_length=255, null=True)

    class Meta:
        permissions = (
            ("view_stock", "Can view the Stock"),
        )

    def __str__(self):
        return str(self.department)

    def get_absolute_url(self):
        return reverse('TODO_name:stock_edit', kwargs={'pk': self.pk})


class Product(models.Model):
    stockKeepingUnit = models.ForeignKey(to='StockKeepingUnit')
    category = models.ForeignKey(to='Category')
    vendor = models.ForeignKey(to='Vendor')
    productName = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=255, null=True)

    class Meta:
        permissions = (
            ("view_product", "Can view the Product"),
        )

    def __str__(self):
        return str(self.stockKeepingUnit)

    def get_absolute_url(self):
        return reverse('TODO_name:product_edit', kwargs={'pk': self.pk})


class Category(models.Model):
    subcategory = models.ForeignKey(to='Category',blank=True, null=True, related_name='children')
    categoryName = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=200, null=True)

    class Meta:
        permissions = (
            ("view_category", "Can view the Category"),
        )

    def __str__(self):
        return str(self.subcategory)

    def get_absolute_url(self):
        return reverse('TODO_name:category_edit', kwargs={'pk': self.pk})


class StockKeepingUnit(models.Model):
    stock = models.ForeignKey(to='Stock')
    available = models.DecimalField(decimal_places=2, null=False, max_digits=10)
    reserved = models.DecimalField(decimal_places=2, null=False, max_digits=10)

    class Meta:
        permissions = (
            ("view_stockkeepingunit", "Can view the StockKeepingUnit"),
        )

    def __str__(self):
        return str(self.stock)

    def get_absolute_url(self):
        return reverse('TODO_name:stockkeepingunit_edit', kwargs={'pk': self.pk})


