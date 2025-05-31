import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,11))
sample = random.sample(numbers, 3)

print(f"Sample: {sample}")