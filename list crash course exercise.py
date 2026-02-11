# Write the following Python code to do the following
# (Complete ALL of these using list comprehension)

# 1. Given a list [1, 2, 3, 4], print out all the values in the list.
lst = [1, 2, 3, 4]
[print(x) for x in lst]

# 2. Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
lst = [1,2,3,4]
new_lst = [20*i for i in lst]
[print(x) for x in new_lst]

# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter
#    Expected output: ["E", "T", "M"]
name_list = ["Elie", "Tim", "Matt"]
first_letter_list = [Name[0] for Name in name_list ]
print(first_letter_list)

# 4. Given a list [1, 2, 3, 4, 5, 6], return a new list of all the even values
#    Expected output: [2, 4, 6]
num_list = [1,2,3,4,5,6]
even_list = [num for num in num_list if num%2==0]
print(even_list)

# 5. Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that is the intersection of the two
#    Expected output: [3, 4]
first_list = [1,2,3,4]
second_list = [3,4,5,6]
new_list = [num for num in first_list if num in second_list]
print(new_list)

# 6. Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lower case
#    Expected output: ["eile", "mit", "ttam"]
original_list = ["Elie", "Tim", "Matt"]
new_list = [word[::-1].lower() for word in original_list ]
print(new_list)

# 7. Given two strings "first" and "third", return a new list with all the letters present in both words
#    Expected output: ["i", "r", "t"]
print([letter for letter in 'first' if letter in 'third'])

# 8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12
#    Expected output: [12, 24, 36, 48, 60, 72, 84, 96]
print([num for num in range(1,101) if num%12==0])

# 9. Given the string "amazing", return a list with all the vowels removed
#    Expected output: ["m", "z", "n", "g"]
vowels = ['a','e','i','o','u','y']
print([letter for letter in 'amazing' if letter not in vowels])

# 10. Generate a list with the value ...
<<<<<<< HEAD
print([[num for num in range(10)] for i in range(9)] )
=======
print([[num for num in range(10)] for i in range(9)] )
>>>>>>> 1e99de536555cc027d94606cee1670be2b074516
