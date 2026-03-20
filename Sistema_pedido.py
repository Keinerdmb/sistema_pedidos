def calculate_daily_income(orders, products):
    total_income = 0

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]
        price = products[product_id][1]
        total_income += price * quantity

    return total_income

def final_report(orders, customers, products):
    if len(orders) == 0:
        print("No orders registered.")
        return

    total_orders = len(orders)
    total_income = calculate_daily_income(orders, products)

    orders_by_customer = {}
    products_sold = {}

    for order_id in orders:
        customer_id, product_id, quantity = orders[order_id]

        # Agrupar pedidos por cliente
        customer_name = customers[customer_id][0]
        if customer_name not in orders_by_customer:
            orders_by_customer[customer_name] = 0
        orders_by_customer[customer_name] += 1

        # Contar productos vendidos
        product_name = products[product_id][0]
        if product_name not in products_sold:
            products_sold[product_name] = 0
        products_sold[product_name] += quantity

    # Mostrar reporte
    print("\n===== FINAL REPORT =====")
    print("Total orders:", total_orders)
    print("Total income:", round(total_income, 2))

    print("\nOrders by customer:")
    for customer in orders_by_customer:
        print("-", customer, ":", orders_by_customer[customer], "orders")

    print("\nProducts sold:")
    for product in products_sold:
        print("-", product, ":", products_sold[product], "units")

    print("========================")