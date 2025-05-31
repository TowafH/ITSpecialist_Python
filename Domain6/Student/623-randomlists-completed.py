import random

players = ["Cristiano Ronaldo", "Messi", "Neymar"]

sample = random.sample(players, 2)
print(f"Sample: {sample}")

choice = random.choice(players)
print(f"Choice: {choice}")

shuffle = random.shuffle(players)
print(f"Shuffle: {players}")