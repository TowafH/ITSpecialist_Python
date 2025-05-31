from random import randrange
# Output random values from 5 to 19, 10 times
for i in range(10):
    print(f"Odd: {randrange(5,20, 2)}") # Returns Odd Numbers
    print(f"Even: {randrange(6, 20, 2)}") # Returns Even Numbers