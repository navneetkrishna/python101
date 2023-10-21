# Exercise 1:
# Iterate the products list and print the name of all products that have price greater than 25.


products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False,
     'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

filtered_items = ""

for item in products:
    # print(item)

    if item.get("price") > 25:
        # print("Items below 25 are:", item.get("name"))
        filtered_items += item.get("name") + ","

    # values can be fetched without get method,
    # but if provided value is not available it will generate error

    # if item['price'] > 25:
    #     filtered_items += item["name"] + ","

print(filtered_items)
