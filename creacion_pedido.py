#funtion create a order
def create_order(orders,order_id, customer_id, product_order, quantity):
    orders[order_id] = (customer_id, product_order, quantity)
    return orders

#funtion show orders and totals
def show_orders(orders, customers, products):
    if len(orders) == 0:
        print("no orders registered.")
    else:
        for order_id  in orders:
            customer_id, product_id, quantity = orders[order_id]
            customer_name = customers[customer_id][0]
            product_name, price = products[product_id]

            total = price * quantity

            print("\nOrder ID:", order_id)
            print("customer:", customer_name)
            print("product:", product_name)
            print("quantity:", quantity)
            print("total:", round(total, 2))
            print("=======================")


