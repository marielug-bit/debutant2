from collections import Counter

l = [1,1,2,3,3,4,4,5,5]
Counter(l) # see what this returns!

string = "aweosakjdsaldwjdwq"
Counter(string)

s = 'this is such a nice nice nice thing that is nice!'

c = Counter(s.split())

# Counter({'a': 1,
#          'is': 2,
#          'nice': 3,
#          'nice!': 1,
#          'such': 1,
#          'that': 1,
#          'thing': 1,
#          'this': 1})

print(c.items())# list of element,count tuples 
print(c.clear()) # clear all values
print(c.values())
 # see all values