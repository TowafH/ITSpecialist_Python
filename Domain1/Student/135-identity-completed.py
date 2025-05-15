team1 = {
    "color":"red", 
    "rank":1
    }

team2 = team1

team3 = {
    "color":"red", 
    "rank":1
    }

print(team1 is team2) # Output: True b/c this is the SAME object
print(team1 is team3) # Output: False b/c this is a DIFFERENT object, despite the same values

