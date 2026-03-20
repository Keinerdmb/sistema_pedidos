# Order Management System 

## *Description*
This program is a simple order management system for a store. It allows you to:

- Register customers
- Create orders
- Display a final with total income and sales

The program uses **dictionaries** and **tuples** only

## *Data structures*
The system uses three main dictonaries:

custumers = {}
products = {}
orders = {}

**The dictonary one** (customers) store customer information
**The dictonary two** (products) store menu information as a name and price
**The dictonary three** (orders) store orders made by customers

## *Funtions*
### 1. Register customers

       def regiister_customer(customers, customer_id, name):

- Store a customer using a tuple (name,)
- Adds the customer to the customers dictonary

### 2. Load products

       def load_products(products):

- initializes the menu
- Each products is stored as:
    (name, price)

**Example:**
    product[1] = ("Agua", 2000)

#### 3. Show products

        def show_products(products):

- Display all avaliable drinks
- Shows ID, name, and price

### 4. Create order

        def create_order(ordes, customer, products, order_id):

- Request customer ID
- Validates if customer exists
- Displays product menu
- Request product and quantity
- Saves order as a tuple:
    (customer_id, product_id, quantity)

### 5. Calculate daily income

        def calculate_daily_income(orders, products)

- Calculates total income from all orders

### 6. Final report

        def final_report(orders, customer, products):

- Total number of orders
- Total income
- Orders grouped by customer
- Products sold (units)

## *Main program*
The main funtion controls the program flow using a menu
    
    def main():

- 1. Register customer
- 2. Create order
- 3. Final report
- 4. Exit

It uses a while loop to allow multiple operations until the users exist

## *Program execution*
This starts the system and allows user interaction

    main():
   
## *Requirements* 

- Python 3.
- No lists used
- Uses dictonaries and tuples

> The project is currently operational and is demonstrating a process of an order management system.