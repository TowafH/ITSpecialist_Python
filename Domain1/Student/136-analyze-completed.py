x = 5
y = 3
#        --True----     -----True-----    ---True---
result = x == 3 + 2 and y in [1, 2, 3] or x is not y
print(result) # Output: True
# True and True or True