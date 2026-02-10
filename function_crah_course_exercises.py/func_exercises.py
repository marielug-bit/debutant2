# EXERCISES – Write the following functions

# difference
# This function takes in two parameters and returns the difference between the two.
# difference(2, 2)  -> 0
# difference(0, 2)  -> -2
def difference (a,b):
    result = a-b
    return result


# print_day
# This function takes in one parameter (a number from 1–7)
# and returns the day of the week:
# 1 = Sunday, 2 = Monday, 3 = Tuesday, etc.
def print_day (x):
    week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    dico = dict(zip(range(1,8),week_days))
    return dico.get(x)
    
# If the number is less than 1 or greater than 7, return None.
# print_day(4)   -> "Wednesday"
# print_day(41)  -> None


# last_element
# This function takes in one parameter (a list)
# and returns the last value in the list.
# If the list is empty, return None.
def last_element(lst):
    if lst == [] :
        return None
    else:
        return lst[-1]
# last_element([1,2,3,4]) -> 4
# last_element([])        -> None


# number_compare
# This function takes in two numbers.
# If the first is greater, return "First is greater."
# If the second is greater, return "Second is greater."
# Otherwise, return "Numbers are equal."
def number_compare(a,b):
    if a>b:
        return 'First is greater'
    if a<b:
        return 'Second is greater'
    if a==b:
        return "Numbers are equal."
# number_compare(1,1) -> "Numbers are equal"
# number_compare(1,2) -> "Second is greater"
# number_compare(2,1) -> "First is greater"


# single_letter_count
# This function takes in two strings: a word and a letter.
# It returns the number of times the letter appears in the word.
# It should be case insensitive.
# If the letter is not found, return 0.
# single_letter_count("amazing", "A") -> 2
def single_letter_count(word,letter):
    return word.count(letter.lower())

# multiple_letter_count
# This function takes in one string
# and returns a dictionary where keys are letters
# and values are the number of times each letter appears.
# multiple_letter_count("hello")  -> {'h':1, 'e':1, 'l':2, 'o':1}
# multiple_letter_count("person") -> {'p':1, 'e':1, 'r':1, 's':1, 'o':1, 'n':1}
def multiple_letter_count(word):
    return {letter : single_letter_count(word,letter) for letter in word}

# list_manipulation
# This function takes four parameters: a list, a command, a location, and a value.
#
# If command == "remove" and location == "end":
#   remove the last item and return it
# If command == "remove" and location == "beginning":
#   remove the first item and return it
# If command == "add" and location == "beginning":
#   add the value to the start of the list and return the list
# If command == "add" and location == "end":
#   add the value to the end of the list and return the list
#
def list_manipulation(lst, command, location, value=None):
    if command == "remove" and location == "end":
        return lst.pop()
    if command == "remove" and location == "beginning":
        return lst.pop(0)
    if command == "add" and location == "beginning":
        lst.insert(0,value)
        return lst
    if command == "add" and location == "end":
        lst.append(value)
        return lst
    
    
# list_manipulation([1,2,3], "remove", "end")        -> 3
# list_manipulation([1,2,3], "remove", "beginning") -> 1
# list_manipulation([1,2,3], "add", "beginning", 20)-> [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30)      -> [1,2,3,30]


# is_palindrome
# A palindrome reads the same forwards and backwards.
# This function takes in one parameter and returns True or False.
# Bonus: ignore spaces and capitalization.
# is_palindrome("testing") -> False
# is_palindrome("tacocat") -> True
# is_palindrome("hannah")  -> True
# is_palindrome("robert")  -> False
# is_palindrome("a man a plan a canal Panama") -> True
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned[::-1] == cleaned


# frequency
# This function takes a list and a search_term
# and returns how many times the search_term appears.
# frequency([1,2,3,4,4,4], 4) -> 3
# frequency([True, False, True, True], False) -> 1
def frequency(lst,value):
    return lst.count(value)


# flip_case
# This function takes a string and a letter
# and reverses the case of all occurrences of that letter.
# flip_case("Hardy har har", "h") -> "hardy Har Har"
def flip_case(string, letter):
    result = ""
    for char in string:
        if char.lower() == letter.lower():
            result += char.swapcase()
        else:
            result += char
    return result
            

# multiply_even_numbers
# This function takes a list of numbers
# and returns the product of all even numbers.
# multiply_even_numbers([2,3,4,5,6]) -> 48
def multiply_even_numbers(lst):
    result = 1
    for number in lst:
        if number%2 == 0:
            result = result*number
    return result


# mode
# This function takes a list of numbers
# and returns the most frequent number.
# You can assume the mode is unique.
# mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) -> 4
def mode(lst):
    starting_frequency = 0
    val = None
    for value in lst:
        if frequency(lst,value) > starting_frequency:
            starting_frequency = frequency(lst,value)
            val = value
    return val


# capitalize
# This function takes a string
# and returns it with the first letter capitalized.
# capitalize("tim")  -> "Tim"
# capitalize("matt") -> "Matt"
def capitalize(word):
    return word.capitalize()


# compact
# This function takes a list
# and returns a list of only truthy values.
# compact([0,1,2,"",[],False,{},None,"All done"])
# -> [1, 2, "All done"]
def compact(lst):
    result = []
    for item in lst:
        if item:
            result.append(item)
    return result


# partition
# This function takes a list and a callback function.
# If the callback returns True, the element goes in the first list.
# Otherwise, it goes in the second list.
# Return both lists inside one list.

def partition(lst, func):
    true_list = []
    false_list = []
    for i in lst:
        if func(i):
            true_list.append(i)
        else:
            false_list.append(i)
    return [true_list, false_list]
#
# def is_even(num):
#     return num % 2 == 0
#
# partition([1,2,3,4], is_even) -> [[2,4], [1,3]]
#def partition(lst, func):
    #return [
        #[x for x in lst if func(x)],
        #[x for x in lst if not func(x)]


# intersection
# This function takes two lists
# and returns a list of values common to both.
# intersection([1,2,3], [2,3,4]) -> [2,3]
def intersection(lst1, lst2):
    result = []
    for item in lst1:
        if item in lst2:
            result.append(item)
    return result

# once
# This function takes a function
# and returns a new function that can only be called once.
# After the first call, it should return None.
#
# def add(a,b):
#     return a + b
#
# one_addition = once(add)
# one_addition(2,2)   -> 4
# one_addition(2,2)   -> None
# one_addition(12,200)-> None


# SUPER BONUS
# Research decorators and refactor "once" into a decorator.
#
# @run_once
# def add(a,b):
#     return a + b
#
# add(2,2)   -> 4
# add(2,20)  -> None
# add(12,20) -> None