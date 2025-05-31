class Game_Player:
    def __init__(self, name):
        self.name = name       # Set the player's name
        self.score = 0         # Start with score 0

    def get_score(self, interval=10):
        self.score += interval
        return self.score

# Create a player named Robin
game_player1 = Game_Player("Robin")

# Test the methods
print(game_player1.get_score())      # ➜ 10
print(game_player1.get_score(100))   # ➜ 110
