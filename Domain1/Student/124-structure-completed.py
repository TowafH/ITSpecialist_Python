#Dictionary
'''
- Stores collections of key-value pairs
- Mutable, items can be added, removed, or changed after creation
- Created using braces --> {}
- Accessed using their keys in brackets []

keys(): Returns a view object that displays a list of all the keys in the dictionary.
values(): Returns a view object that displays a list of all the values in the dictionary.
items(): Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
get(key, default): Returns the value for the specified key if it exists, otherwise returns the default value.
update(other_dict): Updates the dictionary with the key-value pairs from another dictionary.
pop(key, default): Removes the key and returns the corresponding value, or returns the default if the key is not found.
clear(): Removes all items from the dictionary.
'''
coins = {
    "gold":100,
    "silver":50,
    "bronze":25
}
print(coins)

#Set
'''
- An unordered collection of unique elements
- Mutable, items within a set can be added or removed
- Created using braces --> {}
- An empty set must be created using set() because {} will create an empty dictionary
- NO DUPLICATE VALUES **

union_set = set4 | set 5                 --> letters in a or b or both
intersection_set = set4 & set5           --> letters in both a and b
difference_set = set4 - set5             --> letters in a but not in b
symmetric_difference_set = set4 ^ set5   --> letters in a or b but not both
'''
regions = {"north","south","east"}
print(regions)

#Tuple
'''
- An ordered collection of items
- Immutable, elements within tuple CANNOT be changed
- Created using parantheses --> ()
- Tupes can contain elements of different data types
- A single element tupe requires a comma --> tuple_1_element = (1,)
- CAN HAVE DUPLICATE VALUES
'''
char1_name=("Humphrey",'Cat')
char1_name[1]= "Dog" # Element's in a TUPLE cannot be changed
