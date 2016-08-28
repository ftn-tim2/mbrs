"TODO_name"
css="http://bootswatch.com/lumen/bootstrap.min.css"
"City" {
  foreignKey "enterprise" ( To = "Enterprise" )  
  
  char "name" ( max_length = 30,  null = false ) 
  char "zipCode" ( max_length = 12,  null = false ) 
  foreignKey "department" ( To = "Department" )  
  foreignKey "vendor" ( To = "Vendor" )  
  foreignKey "order" ( To = "Order" )  
  foreignKey "customer" ( To = "Customer" )  
}

"Enterprise" {
  char "name" ( max_length = 50,  null = false ) 
  char "address" ( max_length = 150,  null = false ) 
  foreignKey "department" ( To = "Department" )  
  
}

"State" {
  foreignKey "city" ( To = "City" )  
  char "name" ( max_length = 25,  null = false ) 
}

"Department" {
  char "departmentName" ( max_length = 20,  editable = true,  null = false ) 
  char "address" ( max_length = 155,  null = false ) 
  
  foreignKey "stock" ( To = "Stock" )  
  
}

"Vendor" {
  foreignKey "product" ( To = "Product" )  
  char "name" ( max_length = 30,  null = false ) 
  char "address" ( max_length = 150,  null = false ) 
  
}

"OrderItem" {
  
  
  float "orderedQuantity" ( editable = true,  decimal_places = 2,  null = false,  max_digits = 15 ) 
  float "available" ( editable = true,  decimal_places = 2,  null = true,  max_digits = 15 ) 
  float "unitPrice" ( editable = true,  decimal_places = 2,  null = false,  max_digits = 15 ) 
  float "unitTax" ( editable = true,  decimal_places = 2,  null = false,  max_digits = 15 ) 
  float "value" ( editable = true,  decimal_places = 2,  null = false,  max_digits = 10 ) 
}

"Order" {
  foreignKey "orderItem" ( To = "OrderItem" )  
  foreignKey "payment" ( To = "Payment" )  
  foreignKey "invoice" ( To = "Invoice" )  
  int "orderNumber" ( null = false ) 
  dateTime "orderDate" ( null = false ) 
  text "shipmentAddress" ( max_length = 200,  null = false ) 
  int "orderTotal" ( null = false ) 
  char "orderStatus" ( max_length = 30,  null = false,  choices = ((ORDERING,'ordering'),(FINISHED,'finished'),(CANCELED,'canceled'),(SHIPPED,'shipped')) ) 
  
  
}

"PriceListItem" {
  
  
  float "price" ( decimal_places = 2,  null = false,  max_digits = 10 ) 
  float "tax" ( decimal_places = 2,  null = false,  max_digits = 10 ) 
}

"Payment" {
  
  char "paymetMethod" ( max_length = 50,  choices = ((CASH,'cash'),(CREDITCARD,'creditCard'),(PAYPAL,'payPal')) ) 
  dateTime "dateReceived" ( null = false ) 
  float "amountReceived" ( max_length = 9,  editable = false,  null = false ) 
  boolean "canceled" ( null = false ) 
}

"Invoice" {
  
  int "invoiceNumber" ( null = false ) 
  dateTime "invoiceDate" ( ) 
  text "invoiceTotal" ( max_length = 300,  null = true ) 
  boolean "canceled" ( ) 
}

"Customer" {
  char "name" ( max_length = 31,  null = false ) 
  char "address" ( max_length = 51,  null = false ) 
  foreignKey "order" ( To = "Order" )  
  
}

"PriceList" {
  foreignKey "priceListItem" ( To = "PriceListItem" )  
  int "listNumber" ( null = false ) 
  dateTime "activeFromDate" ( null = false ) 
}

"Stock" {
  
  foreignKey "stockKeepingUnit" ( To = "StockKeepingUnit" )  
  char "stockName" ( max_length = 20,  null = false ) 
  text "desription" ( max_length = 255,  null = true ) 
}

"Product" {
  
  
  foreignKey "priceListItem" ( To = "PriceListItem" )  
  
  foreignKey "orderItem" ( To = "OrderItem" )  
  char "productName" ( max_length = 25,  null = false ) 
  text "description" ( max_length = 255,  null = true ) 
}

"Category" {
  foreignKey "product" ( To = "Product" )  
  foreignKey "category" ( To = "Category" )  
  
  char "categoryName" ( max_length = 25,  null = false ) 
  text "description" ( max_length = 200,  null = true ) 
}

"StockKeepingUnit" {
  
  foreignKey "product" ( To = "Product" )  
  float "available" ( decimal_places = 2,  null = false,  max_digits = 10 ) 
  float "reserved" ( decimal_places = 2,  null = false,  max_digits = 10 ) 
}

