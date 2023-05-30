# Using Functions for Swapping Variables

# Method 1: Using Temporary Variables
x = int(input(" Enter a value for x : "))
y = int(input(" Enter a value for y : "))
print( " The Value of x and y before the swap", x,y)
swap = x
x = y
y = swap 

print(" The value of x is : " ,x)
print(" The value of y is : " ,y)

# Method 2: Without Using a swap variable
x = int(input(" Enter a value for x for method 2: "))
y = int(input(" Enter a value for y for method 2: "))

x, y=y, x
print(" The value of x is for method 2 : " ,x)
print(" The value of y is for method 2: " ,y)

# Method 3: Using a Swap Function

def swap_value(x,y):
    swap = x
    x = y
    y = swap 
    return x, y
numbers = swap_value(
    int(input(" Enter a value for x for method 3 : ")),
    int(input(" Enter a value for y for method 3 : ")))
print(numbers)


