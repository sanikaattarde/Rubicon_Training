# Basic Data Structures in Python

# List
my_list = [1, 2, 3, 3, 4, 5]
print("List:", my_list)

my_list.append(6)
print("List after appending 6:", my_list)

my_list.remove(3)
print("List after removing 3:", my_list)

my_list.insert(4, 10)
print("List after inserting:", my_list)

my_list.extend([7, 8, 9])
print("List after extending:", my_list)

my_list.sort()
print("List after sorting:", my_list)

len(my_list)
print("Length of the list:", len(my_list))

sum(my_list)
print("Sum of the list:", sum(my_list))

max(my_list)
print("Max of the list:", max(my_list))

min(my_list)
print("Min of the list:", min(my_list))

#print 2nd largest num in the list
my_list.sort()
print("2nd largest num in the list:", my_list[-2])

my_list.reverse()
print("List after reversing:", my_list)

#add a num multiple times and print the count of that num in the list
my_list.append(3)
my_list.append(3)
my_list.append(3)
print("List after adding 3:", my_list)
print("Count of 3 in the list:", my_list.count(3))

# Remove duplicates from the list
my_list.sort()
print("List before removing duplicates:", my_list)
my_list = list(set(my_list))
print("List after removing duplicates:", my_list)

print("====================================================================================")

# Tuple
my_tuple = (1, 2, 3, 3, 4, 5)
my_tuple1 = (6, 7, 8, 9, 10)
print("Tuple:", my_tuple)

# Concatination two tuples
my_tuple = my_tuple + my_tuple1
print("Tuple after concatenation(two tuples):", my_tuple)

# add a list to a tuple
my_tuple = my_tuple + tuple([11, 12, 13])
print("Tuple after concatenation with a list:", my_tuple)

#sort a tuple
my_tuple = tuple(sorted(my_tuple))  
print("Tuple after sorting:", my_tuple)

#find the memory usage and size of a tuple
my_tuple_size = my_tuple.__sizeof__()
print( my_tuple_size, "bytes")

#find the memory usage and size of a list
my_list_size = my_list.__sizeof__()
print( my_list_size, "bytes")

# Find duplicate elements in a tuple
my_tuple = (1, 2, 3, 3, 4, 5)
duplicates = set([x for x in my_tuple if my_tuple.count(x) > 1])
print("Duplicate elements in the tuple:", duplicates)




print("=====================================================================================")


# Set 

my_set = {1, 2, 3, 3, 4, 5}
print("Set:", my_set)

my_set.add(6)
print("Set after adding 6:", my_set)

my_set.remove(3)
print("Set after removing 3:", my_set)

my_set.update([7, 8, 9])
print("Set after updating with a list:", my_set)

my_set.discard(10)
print("Set after discarding 10:", my_set)

my_set.pop()
print("Set after popping an element:", my_set)

my_set.clear()
print("Set after clearing:", my_set)    

# check if an element is in the set(user input)(do not use f-string)
element = int(input("Enter an element to check if it is in the set: "))
if element in my_set:
    print(str(element) + " is in the set.")
else:    print(str(element) + " is not in the set.")

# Define two set and diffrence between two sets (show both difference sets)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2}
difference = set1.difference(set2)
difference2 = set2.difference(set1)
print("Set1:", set1)
print("Set2:", set2)
print("Difference between set1 and set2:", difference)
print("Difference between set2 and set1:", difference2)

# Define two set and intersection between two sets
intersection = set1.intersection(set2)
print("Intersection between set1 and set2:", intersection)


# check if a set is a subset of another set
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)
is_subset = set3.issubset(set1)
print("Is set3 a subset of set1?", is_subset)

# Diffrence between & , and - operator in sets
difference_operator = set1 - set2
print("Difference between set1 and set2 using - operator:", difference_operator)

# Dictionary