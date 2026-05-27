#Isaac Infante
#A Grocery Store

#init
items = ["Milk", "Eggs", "Bread", "Butter", "Cheese",
         "Frozen Waffles", "Coffee", "Sugar", "Maple Syrup"]
prices = [3.49, 2.99, 2.79, 3.99, 4.59,
          5.49, 7.99, 2.49, 6.99]
#functions
#Challenge 1
def price_check(item_name):
    if item_name in items:
        index = items.index(item_name)
        return prices[index]
    else:
        return "Item not found"

#Challenge 2
def discount(discount):
    for i in range(len(prices)):
        prices[i] = round(prices[i] * (1 - discount), 2)

#Challenge 3
def filter_by_price(max_price):
    filtered = []
    for i in range(len(items)):
        if prices[i] <= max_price:
            filtered.append(items[i])
    print(filtered)

#main
#black friday-20% off
discount(0.20)

#kid with $2
print("Items the kid can buy:")
filter_by_price(2.00)

#Customer
customer_items = ["Frozen Waffles", "Coffee", "Sugar", "Maple Syrup", "Butter"]
total = 0
for item in customer_items:
    total += price_check(item)

print("Customer total:", round(total, 2))


