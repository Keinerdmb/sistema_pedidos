# Data structures
customers = {}
products = {}
orders = {}

# Register customer
def register_customer(customers, customer_id, name, email):
    customers[customer_id] = (name, email)
    return customers

# Register product
def register_product(products, product_id, name, price):
    products[product_id] = (name, price)
    return products

# Create order
def create_order(orders, order_id, customer_id, product_id, quantity):
    orders[order_id] = (customer_id, product_id, quantity)
    return orders

# Show orders
def show_orders(orders, customers, products):
    if len(orders) == 0:
        return "No hay pedidos registrados."

    result = ""

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]

        # Validate
        if customer_id not in customers:
            result += f"\nPedido {order_id} tiene cliente desconocido.\n"
            continue

        if product_id not in products:
            result += f"\nPedido {order_id} tiene producto desconocido.\n"
            continue

        customer_name = customers[customer_id][0]
        product_name, price = products[product_id]
        total = price * quantity

        result += f"\nID Pedido: {order_id}\n"
        result += f"Cliente: {customer_name}\n"
        result += f"Producto: {product_name}\n"
        result += f"Cantidad: {quantity}\n"
        result += f"Total: {round(total,2)}\n"
        result += "=======================\n"

    return result

# Calculate daily income
def calculate_daily_income(orders, products):
    total_income = 0

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]
        if product_id in products:
            price = products[product_id][1]
            total_income += price * quantity
    return total_income

# Final report
def final_report(orders, customers, products):
    if len(orders) == 0:
        return "No hay pedidos registrados."

    total_orders = 0
    total_income = 0
    orders_by_customer = {}
    products_sold = {}

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]

        # Ignore incomplete orders
        if customer_id not in customers or product_id not in products:
            continue

        customer_name = customers[customer_id][0]
        product_name, price = products[product_id]
        total_orders += 1
        total_income += price * quantity

        orders_by_customer[customer_name] = orders_by_customer.get(customer_name,0) + 1
        products_sold[product_name] = products_sold.get(product_name,0) + quantity

    result = "\n===== REPORTE FINAL =====\n"
    result += f"Total de pedidos: {total_orders}\n"
    result += f"Ingresos totales: {round(total_income,2)}\n"

    result += "\nPedidos por cliente:\n"
    for customer in orders_by_customer:
        result += f"- {customer}: {orders_by_customer[customer]} pedidos\n"

    result += "\nProductos vendidos:\n"
    for product in products_sold:
        result += f"- {product}: {products_sold[product]} unidades\n"

    result += "========================"

    return result


# MAIN MENU
def main():
    running = True

    while running:
        print("\n=== MENÚ ===")
        print("1. Registrar cliente")
        print("2. Registrar producto")
        print("3. Crear pedido")
        print("4. Mostrar pedidos")
        print("5. Reporte final")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            cid = input("ID del cliente: ")
            name = input("Nombre: ")
            email = input("Correo: ")
            register_customer(customers, cid, name, email)
            print("Cliente registrado correctamente.")

        elif option == "2":
            pid = input("ID del producto: ")
            name = input("Nombre del producto: ")
            try:
                price = float(input("Precio: "))
                register_product(products, pid, name, price)
                print("Producto registrado correctamente.")
            except ValueError:
                print(" Precio inválido, intente de nuevo.")

        elif option == "3":
            oid = input("ID del pedido: ")
            cid = input("ID del cliente: ")

            # validate customer
            if cid not in customers:
                print(" Cliente no registrado.")
                continue

            pid = input("ID del producto: ")
            # validate product
            if pid not in products:
                print(" Producto no registrado.")
                continue

            try:
                qty = int(input("Cantidad: "))
                create_order(orders, oid, cid, pid, qty)
                print("Pedido creado correctamente.")
            except ValueError:
                print(" Cantidad inválida, intente de nuevo.")

        elif option == "4":
            print(show_orders(orders, customers, products))

        elif option == "5":
            print(final_report(orders, customers, products))

        elif option == "6":
            print("Saliendo del sistema...")
            running = False

        else:
            print("Opción inválida, intente de nuevo.")


# Run program
main()
