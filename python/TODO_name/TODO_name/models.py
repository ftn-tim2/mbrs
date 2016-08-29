from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class City(models.Model):
    enterprise = models.ForeignKey(to='Enterprise')
    name = models.CharField(max_length=30, null=False)
    zipCode = models.CharField(max_length=12, null=False)
    department = models.ForeignKey(to='Department')
    vendor = models.ForeignKey(to='Vendor')
    order = models.ForeignKey(to='Order')
    customer = models.ForeignKey(to='Customer')

    class Meta:
        permissions = (
            ("view_city", "Can view the City"),
        )

    def __str__(self):
        return str(self.enterprise)

    def get_absolute_url(self):
        return reverse('TODO_name:city_edit', kwargs={'pk': self.pk})


class Enterprise(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=False)
    department = models.ForeignKey(to='Department')

    class Meta:
        permissions = (
            ("view_enterprise", "Can view the Enterprise"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:enterprise_edit', kwargs={'pk': self.pk})


class State(models.Model):
    city = models.ForeignKey(to='City')
    name = models.CharField(max_length=25, null=False)

    class Meta:
        permissions = (
            ("view_state", "Can view the State"),
        )

    def __str__(self):
        return str(self.city)

    def get_absolute_url(self):
        return reverse('TODO_name:state_edit', kwargs={'pk': self.pk})


class Department(models.Model):
    departmentName = models.CharField(max_length=20, editable=True, null=False)
    address = models.CharField(max_length=155, null=False)
    stock = models.ForeignKey(to='Stock')

    class Meta:
        permissions = (
            ("view_department", "Can view the Department"),
        )

    def __str__(self):
        return str(self.departmentName)

    def get_absolute_url(self):
        return reverse('TODO_name:department_edit', kwargs={'pk': self.pk})


class Vendor(models.Model):
    product = models.ForeignKey(to='Product')
    name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=150, null=False)

    class Meta:
        permissions = (
            ("view_vendor", "Can view the Vendor"),
        )

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('TODO_name:vendor_edit', kwargs={'pk': self.pk})


class OrderItem(models.Model):
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
        return str(self.orderedQuantity)

    def get_absolute_url(self):
        return reverse('TODO_name:orderitem_edit', kwargs={'pk': self.pk})


class Order(models.Model):
    orderItem = models.ForeignKey(to='OrderItem')
    payment = models.ForeignKey(to='Payment')
    invoice = models.ForeignKey(to='Invoice')
    orderNumber = models.IntegerField(null=False)
    orderDate = models.DateTimeField(null=False)
    shipmentAddress = models.TextField(max_length=200, null=False)
    orderTotal = models.IntegerField(null=False)
    orderStatus = models.CharField(max_length=30, null=False, choices=(("ordering","ORDERING"),("finished","FINISHED"),("canceled","CANCELED"),("shipped","SHIPPED")))

    class Meta:
        permissions = (
            ("view_order", "Can view the Order"),
        )

    def __str__(self):
        return str(self.orderItem)

    def get_absolute_url(self):
        return reverse('TODO_name:order_edit', kwargs={'pk': self.pk})


class PriceListItem(models.Model):
    price = models.DecimalField(decimal_places=2, null=False, max_digits=10)
    tax = models.DecimalField(decimal_places=2, null=False, max_digits=10)

    class Meta:
        permissions = (
            ("view_pricelistitem", "Can view the PriceListItem"),
        )

    def __str__(self):
        return str(self.price)

    def get_absolute_url(self):
        return reverse('TODO_name:pricelistitem_edit', kwargs={'pk': self.pk})


class Payment(models.Model):
    paymetMethod = models.CharField(max_length=50, choices=(("cash","CASH"),("creditCard","CREDITCARD"),("payPal","PAYPAL")))
    dateReceived = models.DateTimeField(null=False)
    amountReceived = models.DecimalField(max_length=9, decimal_places=2, null=False, max_digits=10)
    canceled = models.BooleanField(null=False)

    class Meta:
        permissions = (
            ("view_payment", "Can view the Payment"),
        )

    def __str__(self):
        return str(self.paymetMethod)

    def get_absolute_url(self):
        return reverse('TODO_name:payment_edit', kwargs={'pk': self.pk})


class Invoice(models.Model):
    invoiceNumber = models.IntegerField(null=False)
    invoiceDate = models.DateTimeField()
    invoiceTotal = models.TextField(max_length=300, null=True)
    canceled = models.BooleanField()

    class Meta:
        permissions = (
            ("view_invoice", "Can view the Invoice"),
        )

    def __str__(self):
        return str(self.invoiceNumber)

    def get_absolute_url(self):
        return reverse('TODO_name:invoice_edit', kwargs={'pk': self.pk})


class Customer(models.Model):
    name = models.CharField(max_length=31, null=False)
    address = models.CharField(max_length=51, null=False)
    order = models.ForeignKey(to='Order')

    class Meta:
        permissions = (
            ("view_customer", "Can view the Customer"),
        )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('TODO_name:customer_edit', kwargs={'pk': self.pk})


class PriceList(models.Model):
    priceListItem = models.ForeignKey(to='PriceListItem')
    listNumber = models.IntegerField(null=False)
    activeFromDate = models.DateTimeField(null=False)

    class Meta:
        permissions = (
            ("view_pricelist", "Can view the PriceList"),
        )

    def __str__(self):
        return str(self.priceListItem)

    def get_absolute_url(self):
        return reverse('TODO_name:pricelist_edit', kwargs={'pk': self.pk})


class Stock(models.Model):
    stockKeepingUnit = models.ForeignKey(to='StockKeepingUnit')
    stockName = models.CharField(max_length=20, null=False)
    desription = models.TextField(max_length=255, null=True)

    class Meta:
        permissions = (
            ("view_stock", "Can view the Stock"),
        )

    def __str__(self):
        return str(self.stockKeepingUnit)

    def get_absolute_url(self):
        return reverse('TODO_name:stock_edit', kwargs={'pk': self.pk})


class Product(models.Model):
    priceListItem = models.ForeignKey(to='PriceListItem')
    orderItem = models.ForeignKey(to='OrderItem')
    productName = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=255, null=True)

    class Meta:
        permissions = (
            ("view_product", "Can view the Product"),
        )

    def __str__(self):
        return str(self.priceListItem)

    def get_absolute_url(self):
        return reverse('TODO_name:product_edit', kwargs={'pk': self.pk})


class Category(models.Model):
    product = models.ForeignKey(to='Product')
    category = models.ForeignKey('Category', blank=True, null=True, related_name='children')
    categoryName = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=200, null=True)

    class Meta:
        permissions = (
            ("view_category", "Can view the Category"),
        )

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('TODO_name:category_edit', kwargs={'pk': self.pk})


class StockKeepingUnit(models.Model):
    product = models.ForeignKey(to='Product')
    available = models.DecimalField(decimal_places=2, null=False, max_digits=10)
    reserved = models.DecimalField(decimal_places=2, null=False, max_digits=10)

    class Meta:
        permissions = (
            ("view_stockkeepingunit", "Can view the StockKeepingUnit"),
        )

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('TODO_name:stockkeepingunit_edit', kwargs={'pk': self.pk})


