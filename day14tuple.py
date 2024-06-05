#1. Write a Python program to find the number of times 4 appears in the tuple. 
#Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) 
#Output: 3 

tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)                    # Define the tuple
count_of_4 = tuplex.count(4)                            # Count the number of occurrences of 4 in the tuple
print("Number of times 4 appears in the tuple:", count_of_4)        # Print the result

#2.Write a Python program to convert a list to a tuple. 
#Input: listx = [5, 10, 7, 4, 15, 3] 
#Output: (5, 10, 7, 4, 15, 3) 

listx = [5, 10, 7, 4, 15, 3]        # Define the list

tuplex = tuple(listx)               # Convert the list to a tuple

print("Tuple:", tuplex)             # Print the tuple

#3. Write a Python program to calculate the sum of the numbers in a given tuple. 
#Input: tuples_list = [(1, 2), (3, 4), (5, 6)]

tuples_list = [(1, 2), (3, 4), (5, 6)]                  # Define the input tuple list

total_sum = 0                                               # Initialize the variable to store the sum

for tup in tuples_list:                                     # Iterate through each tuple in the list
    total_sum += sum(tup)                                        # Sum the elements of each tuple and add to the total sum

print("Sum of numbers in the given tuple list:", total_sum)         # Print the total sum

#4.Write a python program and iterate the given tuples
#Input: 
#employee1 = ("John Doe", 101, "Human Resources", 60000) 
#employee2 = ("Alice Smith", 102, "Marketing", 55000) 
#employee3 = ("Bob Johnson", 103, "Engineering", 75000)


employee1 = ("John Doe", 101, "Human Resources", 60000)             # Define the tuples employee1
employee2 = ("Alice Smith", 102, "Marketing", 55000)                 # Define the tuples employee2
employee3 = ("Bob Johnson", 103, "Engineering", 75000)                   # Define the tuples employee3

employees = [employee1, employee2, employee3]                       # Store the tuples in a list

for employee in employees:                                          # Iterate through the list of tuples
    # Print each element of the tuple
    print("Name:", employee[0])                                     # Print each element of the tuple
    print("ID:", employee[1])
    print("Department:", employee[2])
    print("Salary:", employee[3])
    print()                                                           # Adding an empty line 
