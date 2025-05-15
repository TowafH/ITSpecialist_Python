capitals=["Montgomery","Juneau","Phoenix"]

capitals.append("Sacramento") # Output: ['Montgomery', 'Juneau', 'Phoneix', 'Sacramento']

capitals.insert(3, "LittleRock") # Output: ['Montgomery', 'Juneau', 'Phoneix', 'LittleRock', 'Sacramento']

capitals.remove("Juneau") # Output: ['Montgomery', 'Phoneix', 'LittleRock', 'Sacramento']

population=[200000,32000,1600000]

capitals[2]="Little Rock" # Output: ['Montgomery', 'Phoneix', 'LittleRock', 'Sacramento']

capitals.sort(reverse=True) # Output: ['Sacramento', 'Phoenix', 'Montgomery', 'Little Rock']

print(capitals.pop(0)) # Output: Sacramento

print(capitals) # Output: ['Phoenix', 'Montgomery', 'Little Rock']

print(min(population)) # Output: 32000

print(len(capitals)) # Output: 3