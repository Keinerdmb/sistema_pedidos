#data estructures (dictonaries)
customers = {}
products = {}
orders = {}

#funtion register customer
def register_cutomer(customers, customer_id, name):
    #we save the client as a tuple(name)
    customers[customer_id] = (name,)
    print("Cliente registrado con exito.")

#funtion add products (drink's menu)
def load_products(products):
    #drink's menu (ID: (name,price))
    products[1] = ("Agua", 2000)
    products[2] = ("Soda", 3500)
    products[3] = ("Jugo", 4000)
    products[4] = ("Café", 2500)

#funtion show products
def show_products(products):
    print("/n=== MENU BEBIDAS ===")
    for product_id in products:
        name, price = products[product_id] 
        print(product_id, "-", name, "$", price)

#funtion create a order 
def create_order(orders, customers, products, order_id):
    customer_id = int(input("Ingrese ID del cliente: "))

    #validate client
    if customer_id not in customers:
        print("Cliente no existe.")
        return
    
    #show menu
    show_products(products)

    product_id = int(input("Escoge un producto "))
    quantity = int(input("Ingrese cantidad: "))

    #validate product
    if product_id not in products:
        print("Producto invalido.")
        return
    
    #save the order as a tuple
    orders[order_id] = (customer_id, product_id, quantity)
    print("Pedido añadido  correctamente.")

#funtion calculate income    
def calculate_daily_income(orders, products):
    total_income = 0

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]

        if product_id in products:
            price = products[product_id][1]
            total_income += price * quantity

    return total_income

#funtion final report
def final_report(orders, customers, products):
    if len(orders) == 0:
        print("No hay pedidos registrados.")
        return

    total_orders = len(orders)
    total_income = calculate_daily_income(orders, products)

    orders_by_customer = {}
    products_sold = {}

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]

        #validate
        if customer_id not in customers or product_id not in products:
            continue

        #group orders by customer
        customer_name = customers[customer_id][0]

        if customer_name not in orders_by_customer:
            orders_by_customer[customer_name] = 0
        orders_by_customer[customer_name] += 1

        # Count products sold
        product_name = products[product_id][0]

        if product_name not in products_sold:
            products_sold[product_name] = 0
        products_sold[product_name] += quantity

    #show report
    print("\n===== REPORTE FINAL =====")
    print("Total pedidos:", total_orders)
    print("Total ingresos:", round(total_income, 2))

    print("\nPedidos por cliente:")
    for customer in orders_by_customer:
        print("-", customer, ":", orders_by_customer[customer], "pedidos")

    print("\nProductos vendidos:")
    for product in products_sold:
        print("-", product, ":", products_sold[product], "unidades")

    print("========================")

#main program (menu)
def main():
    load_products(products)

    order_id = 1
    option = 0

    while option != 4:
        print("/n=== MENU ===")
        print("1. Registar cliente")
        print("2. Crear pedido")
        print("3. Reporte final")
        print("4. salida")

        option = int(input("Escoge una opción: "))

        if option == 1:
            customer_id = int(input("Ingrese ID del cliente: "))
            name = input("Ingrese nombre del cliente: ")
            register_cutomer(customers, customer_id, name)

        elif option == 2:
            create_order(orders, customers, products, order_id)
            order_id += 1

        elif option == 3:
            final_report(orders, customers, products)

        elif option == 4:
            print("Saliendo del programa...")

        else:
            print("Opción invalida.")

#run program
main()