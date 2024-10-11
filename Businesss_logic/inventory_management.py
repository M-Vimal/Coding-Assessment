products = [
    {"id": 1, "name": "Product A", "stock": 20},
    {"id": 2, "name": "Product B", "stock": 15},
    {"id": 3, "name": "Product C", "stock": 30}
]

sales_orders = [
    {"product_id": 1, "quantity": 25},
    {"product_id": 2, "quantity": 17},
    {"product_id": 3, "quantity": 33}  
]
min_stock = 10
def process_orders(products,sales_orders):
    product_dist = {product['id']:product for product in products}
    print(product_dist)
    restock_alert=[]

    for order in sales_orders:
        product_id = order["product_id"]
        quantity = order["quantity"]

        if product_id not in product_dist:
            print("product is not exists")
            continue

        product = product_dist[product_id]
        if product['stock']>=quantity:
            product['stock']-=quantity
            print(f"{product["name"]},order successful")

            if product['stock']<min_stock:
                restock_alert.append(product)
 
        else:
            print(f"Insufficient stock for {product['name']}. Only {product['stock']} units left, but {quantity} ordered.")
    return restock_alert
   
    
process_orders(products,sales_orders)

def restock_items(products,restock_list):
    products_dict = {product['id']: product for product in products}

    for restock in restock_list:
        product_id = restock['product_id']
        restock_quantity = restock['quantity']

        if product_id not in products_dict:
            print(f"Error: Product ID {product_id} does not exist for restocking.")
            continue

        product = products_dict[product_id]
        product['stock'] += restock_quantity
        print(f"Restocked {restock_quantity} units of {product['name']}. New stock: {product['stock']} units.")
        



# Restocking items when stock reduces

# restock_list = [
#     {"product_id": 2, "quantity": 20},  # Restock Product B
#     {"product_id": 3, "quantity": 50}   # Restock Product C
# ]

#restock_items(products, restock_list)



