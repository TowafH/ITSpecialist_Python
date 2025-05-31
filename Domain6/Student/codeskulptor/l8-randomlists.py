import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,11))
print(f"Original: {numbers}")

random.shuffle(numbers)

print(f"Shuffled: {numbers}")