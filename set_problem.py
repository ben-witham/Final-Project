############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of sets
#          and their useful functions
# 
############################################################

# This exercise consists of three parts
# In this problem, you will need to determine if two sets have nothing in common

set1 = {3,5,2,7,9}
set2 = {5,7,9}
set3 = {1,4,8}
set4 = {2,3,8}
set5 = {2,3}
set6 = {5,7}

def no_similar_numbers(set1, set2):
    pass

print("Problem 1")
print(no_similar_numbers(set1, set2)) # False
print(no_similar_numbers(set1, set3)) # True
print(no_similar_numbers(set1, set4)) # False
print(no_similar_numbers(set4, set5)) # False

# In this problem, find all the data that only one set has

def set_differences(set_of_difference, other_set):
    pass

print("Problem 2")
print(set_differences(set2, set1)) # {2,3}
print(set_differences(set4, set1)) # {9,5,7}
print(set_differences(set1, set6)) # {4}

# In this problem, find if one set is a subset of another set (You will need to look this up)

def is_subset(megaset, subset):
    pass

print("Problem 3")
print(is_subset(set1, set2)) # False
print(is_subset(set2, set1)) # True
print(is_subset(set3, set1)) # False
print(is_subset(set4, set1)) # False
print(is_subset(set5, set4)) # True