def calculate_total(product_cost,location):
    product_cost = float(input("Enter the product cost: "))
    location = str(input("Enter your location (USA, Europe, Canada, other): "))
    if location.upper() == "USA":
        Shipping_cost = 5
    elif location.upper() == "Europe":
        Shipping_cost = 7
    elif location.upper() == "CANADA":
        Shipping_cost = 3
    else:
        Shipping_cost = 9
    total_cost = Shipping_cost + product_cost
    return total_cost