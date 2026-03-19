customers = {}
products = {}
orders = {}

#Function to register a customer

def register_customer(customers, customer_id, name, email):
    customers[customer_id] = (name, email)
    return  customers

#Function to register a product

def register_products(products, product_id, name, price):
    products[product_id]= (name, price)
    return products


