def is_prime(num):
# To check if a number is prime or not 
    if num < 2:
       return False
    for a in range(2, num):
        if num % a == 0:
           return False
    return True

print (is_prime(5))
