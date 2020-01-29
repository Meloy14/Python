# ----------------------------------------------------------------------------------------
# Sample 01: Dictionary Basic
# ----------------------------------------------------------------------------------------
sample_01_1 = {
    "name": "Colt",
    "own_dog": True,
    "courses": 4,
    44: "my number!"
}
# Another approach is to use the 'dict' function You assign values to keys by passing in 
# keys and values separated by an =
sample_01_2 = dict(name="kitty", age=0.5)
print(f"Samp_01: {sample_01_1}") # Output: Samp_01: {'name': 'Colt', 'own_dog': True, 
                                 #                  'courses': 4, 44: 'my number!'}
print(f"Samp_01: {sample_01_2}") # Output: Samp_01: {'name': 'kitty', 'age': 0.5}
# Accessing Individual Values
print(f"Samp_01: {sample_01_1['name']}") # Output: Samp_01: Colt
# Accessing All Values in a Dictionary Use .values()
for value in sample_01_1.values():
    print(value) # Output: Colt True 4 my number!
# Accessing All Keys in a Dictionary Use .keys()
for key in sample_01_1.keys():
    print(key) # Output: name own_dog courses 44
# Accessing All Keys and Values in a Dictionary Use .items()
for key,value in sample_01_1.items():
    print(key,value) # Output: name Colt - own_dog True - courses 4 - 44 my number!
# To check if Key or Value is inside Dictionary
print(f"Key in {'name' in sample_01_1}") # True
print(f"Key in {'awesome' in sample_01_1}") # False
print(f"Value in {'Colt' in sample_01_1.values()}") # True
print(f"Value in {'Nope!' in sample_01_1.values()}") # False

      
      
# ----------------------------------------------------------------------------------------
# Sample 02: Dictionary Methods
# ----------------------------------------------------------------------------------------
# Clear - Clears all the keys and values in a dictionary
d = dict(a=1,b=2,c=3)
d.clear()
d # {}
# Copy - Makes a copy of a dictionary
d = dict(a=1,b=2,c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
c is d # False
# fromkeys - Creates key-value pairs from comma separated values:
{}.fromkeys("a","b") # {'a': 'b'}
{}.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
fromkeyVar = {}.fromkeys(['email', 'score', 'profile'], 'unknown')
print(f"fromkeys - {fromkeyVar}") # {'email': 'unknown', 'score': 'unknown', 'profile': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}
print(f"fromkeys - {dict.fromkeys('test', 'unknown')}")
print(f"fromkeys - {dict.fromkeys(range(1,5), 'NA')}")
# Get - Retrieves a key in an object and return None instead of a KeyError if the key does not exist:
d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['b'] # 2
d.get('b') # 2
# d['no_key'] # KeyError
d.get('no_key') # None
# Pop - Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. 
# Returns the value corresponding to the key that was removed.
d = dict(a=1,b=2,c=3)
# d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
print(f"pop - {d}") # {'b': 2, 'c': 3}
# d.pop('e') # KeyError
# Popitem - Removes a random key in a dictionary:
d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ('d', 4)
# d.popitem('a') # TypeError: popitem() takes no arguments (1 given)
# Update - Update keys and values in a dictionary with another set of key value pairs.
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}
second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# let's overwrite an existng key
second['a'] = "AMAZING"
# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# the update overrides our values
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

      
      
# ----------------------------------------------------------------------------------------
# Sample 03: Dictionary Comprehension
# the syntax
# { ____:____ for ___ in ____}
# - iterates over keys by default
# - to iterate over keys and values using .items()
# ----------------------------------------------------------------------------------------
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
# More Examples
squared_numbers = {num: num**2 for num in [1,2,3,4,5]}
print(squared_numbers) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# More Examples
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}
# More Examples
instructor = {"name": "colt", "city": "san francisco", "color": "purple"}
yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(yelling_instructor) # {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}
# Conditional logic with dictionaries
num_list = [1,2,3,4]
new_num_list = { num:("even" if num % 2 == 0 else "odd") for num in num_list }
print(new_num_list) # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
# More conditional logic examples
instructor = {"name": "colt", "city": "san francisco", "color": "purple"}
yelling_instructor = {k.upper() if k is "color" else k: v.upper() for k,v in instructor.items()}
print(yelling_instructor) # {{'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
