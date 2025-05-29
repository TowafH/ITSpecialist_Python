def total_score(score, multiplier=1.5):
    return score * multiplier

print(total_score(3000)) # Output: 4500.0
print(total_score(4000,2)) # Output: 8000
print(total_score(multiplier=3, score=15000)) # Output: 45000