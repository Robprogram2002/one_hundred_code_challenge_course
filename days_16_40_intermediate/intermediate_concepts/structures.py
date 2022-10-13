# *********************** LISTS *************************

# List can have items of different data types
from typing import List

first_list: List[str] = ["apple", "strawberry", "banana"]

print(first_list[-1])
print(first_list[-3])  # count the items from right to left starting in one

for item in first_list:
    print(item)

# check if an item is in a list
if "banana" in first_list:
    print("Yes")
else:
    print("No")

first_list.reverse()
print("reverse order of the list", first_list)

first_list.sort()  # here we are changing the original list
print("sorted order of the list", first_list)

new_list = sorted(first_list)
print("the new order list", new_list)

# methods :
# pop -> delete the last item
# remove -> delete an item from certain index
# clear -> clear the list, delete all items
# append -> add an item to the end of the list
# insert -> add an item in a certain index
# reverse -> reverse the order in a list


# Slicing
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(number_list[1:5])  # the last index is excluded, but the first is included
print(number_list[:3])  # if no especify the first index then begins from the start
print(number_list[2:])  # if not specify the last index it goes away until the end
print(number_list[::2])  # the third number represent the steps of the iteration
print(number_list[::-2])  # we can also use negative index

# Copying a list

# here we are not copying the list, but we are just creating a new pointer for the same list in memory
# if we modify the "second_list" variable we also modify the first and the list itself
second_list = first_list
second_list.append("pineapple")
print(second_list)
print(first_list)

# here we are in true copying the list (so we are creating a new list in memory, not a pointer to an existing list)
list_copy = first_list.copy()
list_copy.append("lemon")
print(list_copy)
print(first_list)

# we can also copy a list using these other syntax
# list_copy = list(first_list)
# list_copy = first_list[:]

# LIST  COMPREHENSIONS
power_list: List[int] = [i * i for i in number_list]
print(power_list)

# ****************** TUPLES ********************

# tuples can have items of different types, they are index ordered, immutable, allow duplicate elements
first_tuple = ("Robert")  # this is not recognise as a tuple instead just as a string
print(type(first_tuple))

first_tuple = ("Robert",)  # with this comma this is already recognise as a tuple
print(type(first_tuple))

# we can create a tuple from the tuple function
first_tuple = tuple(["Robert", 18, "Mexico"])
letters_tuple = ("a", "b", "c", "x", "b", "c", "y")

# Methods

# count -> count how many times an element is in the tuple
print(letters_tuple.count("b"))

# index -> return the index of the first occurrence for a given element in the tuple
print(letters_tuple.index("c"))  # if the element is not in the tuple a given is thrown

# toda la manipulación que se hizo con las listas

# We can assign many items in the tuple at the same time,
# but the variables have to be many as elements in the tuple
item1, item2, item3 = first_tuple
print(item1)
print(item2)
print(item3)

# here, item1 is the first element in te tuple and item3 the last. But item2 is a list with all the  elements in between
# that are in the tuple
item1, *item2, item3 = letters_tuple
print(item1)
print(item2)
print(item3)

# ****************** Dictionary ********************
custom_dict = {"name": "Robert", "age": 28, "city": "New York"}

# if we want to delete a key-value pair we have two options
print(custom_dict)
del custom_dict["name"]
custom_dict.pop("age")
print(custom_dict)

# custom_dict.popitem()  , this remove the last item

custom_dict = {"name": "Robert", "age": 28, "city": "New York"}
# check if a key is in the dictionary
if "name" in custom_dict:
    print(custom_dict["name"])
else:
    print("no in this dictionary")

# try and except syntax
try:
    print(custom_dict["country"])
except:
    print("Error cached")

# if we loop a dictionary we get a key
for key in custom_dict:
    print(key)

for value in custom_dict.values():
    print(value)

# the two before loops can be done in a single loop
for key, value in custom_dict.items():
    print(key, value)

# as list, if we just asign an existing dictionary to a new variable we only
# create a pointer for the same dictionary in memory. To make  an actual cophy we can use the copy method

new_dictionary = custom_dict.copy()
new_dictionary["country"] = "Mexico"
print(new_dictionary)
print(custom_dict)

# we can merge two dictionaries, the keys in both dicts are not affected but the new ones are added
new_dictionary["gender"] = "male"
custom_dict.update(new_dictionary)
print(custom_dict)

# Keys : we can use integers and floats and strings and tuples for keys in a dictionary,
# but we can not use a list as a key
# for a dictionary since lists are mutable and can be changed after its creation, for that they are unhashable

# ****************** Dictionary ********************

# sets are unordered, mutable , and not permit duplicated elements
my_set = {2, 3, 4, 5, 6}
# here we get an set with the letters of the string with no repetition and without the order
other_set = set("Hello Guys")
print(my_set)
print(other_set)

my_set.add(10)
my_set.remove(2)  # if the element doesn't exist an error is thrown

# **** Methods
# pop -> select and remove an arbitrary item from the set
# clear -> clear the set
# union -> the set union
print(my_set.union({24, 6, 18}))
# intersection -> the set intersection

# intersection_update -> change the original set and left only the elements that are in the intersection
my_set.intersection_update({24, 6, 3, 18})
print(my_set)

# frozeenset -> make a set inmmutable, so if we try to change it an error will be thrown
a = frozenset([1, 2, 4, 5])
# a.add() error

