#1. Write a Python program to sum all the items in a list. 

example_list = [1, 2, 3, 4, 5]                      # Example list

total_sum = sum(example_list)                       # Sum of all items in the list

print("List:", example_list)                        # Display the result
print("Sum of all items:", total_sum)

#2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

example_list = [1, 3, 5, 2, 4]                  # Example list

largest = smallest = example_list[0]            # Initialize variables to store largest and smallest numbers

for num in example_list:                            # Iterate through the list to find the largest and smallest numbers
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("List:", example_list)                # Display the result
print("Largest number:", largest)
print("Smallest number:", smallest)

#3. Write a Python program to find duplicate values from a list and display those. 

def find_duplicates(lst):
    duplicates = []
    seen = set()
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

example_list = [1, 2, 3, 4, 2, 5, 3, 6, 7, 7, 8]        # Example list

duplicate_values = find_duplicates(example_list)        # Find duplicate values

print("List:", example_list)                            # Display the result
print("Duplicate values:", duplicate_values)

#4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
#Original list: [1, 1, 2, 3, 4, 4, 5, 1] 
#Length of the first part of the list: 3 
#Splitted the said list into two parts: 
#([1, 1, 2], [3, 4, 4, 5, 1]) 

def split_list(lst, length):
    return lst[:length], lst[length:]

original_list = [1, 1, 2, 3, 4, 4, 5, 1]    # Original list

first_part_length = 3               # Length of the first part of the list

split_result = split_list(original_list, first_part_length)  # Split the list

print("Original list:", original_list)                                  # Display the result
print("Length of the first part of the list:", first_part_length)
print("Splitted the said list into two parts:")
print(split_result)

#5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order:
#black 
#white 
#green 
#red

original_list = ['red', 'green', 'white', 'black']      # Original list

for index in range(len(original_list) - 1, -1, -1):     # Traverse the list in reverse order
    print(original_list[index])