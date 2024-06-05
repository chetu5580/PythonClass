 #1. Write a Python program to Get Only unique items from two sets. 
#Input: 
#set1 = {10, 20, 30, 40, 50} 
#set2 = {30, 40, 50, 60, 70} 
#Output: {70, 40, 10, 50, 20, 60, 30} 
def Unique_items(set1,set2):
    set=set1 | set2                             #Union  operation using '|' operator
    return set

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
set3 = Unique_items(set1,set2)                  #funtion call 
print(set3)                                     # Prints Set3 

#2. Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input: 
#set1 = {10, 20, 30, 40, 50} 
#set2 = {30, 40, 50, 60, 70}
#Output: {20, 70, 10, 60} 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
set3 =set1^set2                             #symmetric difference (^) operation.
print(set3)                                  # Prints Set3

#3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements. 
#Input: 

#set1 = {10, 20, 30, 40, 50} 
#set2 = {60, 70, 80, 90, 10} 
#Output: {10} 
set1 = {10, 20, 30, 40, 50} 
set2 = {60, 70, 80, 90, 10} 
set3=set1&set2                                 # intersection (&) operation.              
print(set3)                                    # Prints Set3

#4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
#Input: 
#set1 = {10, 20, 30, 40, 50} 
#set2 = {30, 40, 50, 60, 70} 
#Output: {40, 50, 30}
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
set3=set1&set2                                  # intersection (&) operation.
print(set3)                                     # Prints Set3