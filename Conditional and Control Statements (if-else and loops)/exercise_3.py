# Exercise 3:
#     - Create a list of products (product names) that are on sale but do not have a sale price.
#     - If a product is on sale but does not have sale price, you need to let the partner know. So the list of
#         products you generate will be shared with the partner. But for purpose of this exercise, just print the list
#         of sale products without sale price that you created.

products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

product_without_sale_price = []

for item in products:

    # print(item)
    # if item.get("is_on_sale") and (item.get("sale_price") == None):       # same
    # if item.get("is_on_sale") and not (item.get("sale_price")):           # same
    if item.get("is_on_sale") and (item.get("sale_price") is None):         # same
        # print(item)
        product_without_sale_price.append(item.get('name'))

print(product_without_sale_price)