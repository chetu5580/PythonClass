# 1. Print the reverse order series  using a while loop

num = 10                        # initializing num to 10


while num >= 1:                 #Checking wheather num is greater than 1
    print(num)                  # printing num
    num -= 1                    # num = num -1


#2.      Create a code that describe the use of break statement in while loop

count = 0                         # initializing count  to 0


while True:                         # Define a while loop
    
    count += 1                      # Increment the count
    
    
    print("Count:", count)          # Print the current count
    
    
    if count > 5:                    # Check if count exceeds 5
    
        break                           # If count exceeds 5, exit the loop


print("Loop terminated")                # Print a message indicating loop termination
#3.      Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

# Define the string
my_string = "Python"            # Define the string


length = 0                      # Initialize variables length to 0
index = 0                       # Initialize variables index to 0


while index < len(my_string):           # Calculate the length of the string
  
    print(my_string[index])             # Print each character on a new line
    
 
    length += 1                          # Increment the length
    
   
    index += 1                           # Move to the next character


print("Length of the string:", length)      # Print the length of the string

#4.      Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

num = int(input("Enter a number: "))        # Take input from the user

factorial = 1                               # Initialize variables factorial to 1
i = 1                                       # Initialize variables i to 1


while i <= num:                             # Calculate factorial using a while loop
    factorial *= i
    i += 1

# Display the result
print("Factorial of", num, "is:", factorial)    # Display the result
print