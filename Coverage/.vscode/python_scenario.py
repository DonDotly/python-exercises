product_cost = float(input("What is the product cost: "))
location = input("Enter your location (US, Europe, Canada, others): ")
if location.upper() == "US":
    shipping_cost = 5
elif location.upper() == "Europe":
    shipping_cost = 7
elif location.uper() == "Canada":
    shipping_cost = 3
else:
    shipping_cost = 9
total_cost = shipping_cost + product_cost
print(total_cost)