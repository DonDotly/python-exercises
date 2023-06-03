from calculator_total_cost import calculate_total
product_cost = float(input("Enter the product cost : "))
location = (input("Enter your loaction (USA, Europe, Canada other): "))
total_cost = calculate_total(product_cost,location)
print("You have to pay $",total_cost)