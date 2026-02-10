# Write the following Python code to do the following
# (Complete ALL of the following using dictionary comprehension)

# 1. Given a list [("name", "Elie"), ("job", "Instructor")],
#    create a dictionary that looks like this:
#    {'job': 'Instructor', 'name': 'Elie'}
#    (the order does not matter).
Elie_list = [("name", "Elie"), ("job", "Instructor")]
print({tup[0]:tup[1] for tup in Elie_list})

# 2. Given two lists ["CA", "NJ", "RI"] and
#    ["California", "New Jersey", "Rhode Island"],
#    return a dictionary that looks like this:
#    {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
#    You can research the zip method to help you.
Capitals = ["CA", "NJ", "RI"]
Places =  ["California", "New Jersey", "Rhode Island"]
print({Capitals[k]:Places[k] for k in range(3)})
print({c: p for c, p in zip(Capitals, Places)})
# zip(Places, Capitals) = (California, CA) ("New Jersey",NJ) ("Rhode Island",RI)

# 3. Create a dictionary with the key as a vowel in the alphabet
#    and the value as 0.
#    Your dictionary should look like this:
#    {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
#    (Do NOT use the fromkeys method).
vowels = ['a','e','i','o','u']
print({v:0 for v in vowels})


# 4. Create a dictionary starting with the key as the position
#    of the letter and the value as the letter in the alphabet.
#    You should return something like this:
#    {1: 'A', 2: 'B', 3: 'C', ...}
#    Hint: use chr(65) to get the first letter.
print({i+1:chr(65+i) for i in range(26)})

# Super Bonus
# Given the string "awesome sauce",
# return a dictionary with the keys as vowels
# and the values as the count of each vowel.
#
# Your dictionary should look like this:
# {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}
vowels = ['a','e','i','o','u']
print({v:"awesome sauce".count(v) for v in vowels})