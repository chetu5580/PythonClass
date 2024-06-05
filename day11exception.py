
#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 

def divide_numbers(a, b):
    try:                                                            # try block
        result = a / b                                              # Action of a/b which stores in result
        print("Result of division:", result)
    except ZeroDivisionError:                                       # excetions block
        print("Error: Division by zero is not allowed.")                #prints if denominator is 0


numerator = 10                                                      #initialization 
denominator = 0                                                       #initialization 

divide_numbers(numerator, denominator)                                      # function call

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
def get_integer_input():
    while True:
        try:
            user_input = input("Please enter an integer: ")          # Prompt the user to enter an integer
            integer_value = int(user_input)                  # Convert the user input to an integer
            return integer_value                     # If conversion is successful, return the integer value
        
        except ValueError:
            print("Error: Please enter a valid integer.")        # If the conversion fails (e.g., non-integer input), catch the ValueError
try:
    integer_input = get_integer_input()                 # Call the get_integer_input function to prompt the user for input
    print("You entered:", integer_input)                # Print the integer entered by the user

except ValueError:
    print("Error: Input is not a valid integer.")        # Handle the ValueError exception if the input is not a valid integer

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 
def read_file(filename):
    try:
       
        with open(filename, 'r') as file:                   # Attempt to open the file in read mode
            content = file.read()                            # If the file exists, read its content
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file '{}' does not exist.".format(filename))      # If the file does not exist, handle the FileNotFoundError

filename = input("Enter the name of the file to read: ")        # Prompt the user to enter the filename

read_file(filename)                     # Call the read_file function with the provided filename

#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
def get_numerical_input(prompt):
  
    while True:                                          # Loop until valid numerical input is provided
        try:
            value = float(input(prompt))                 # Try to convert input to float
            return value                             # Return the numerical value
        except ValueError:
           
            print("Error: Please enter a numerical value.")      # If conversion fails, print error message and continue looping

try:
    
    num1 = get_numerical_input("Enter the first number: ")           # Get numerical input for the first number
   
    num2 = get_numerical_input("Enter the second number: ")         # Get numerical input for the second number
except TypeError:
    print("Error: Inputs are not numerical.")                        # Handle TypeError if inputs are not numerical

   
  
