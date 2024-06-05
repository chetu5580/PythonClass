#1. Print the first 10 natural numbers using for loop 

for i in range(1, 11):                             # Using a for loop to print the first 10 natural numbers
    print(i)

#2. Python program to check if the given string is a palindrome 

def is_palindrome(s):
    
    s = s.replace(" ", "").lower()              # Remove spaces and convert to lowercase for case-insensitive comparison
    return s == s[::-1]                          # Compare the string with its reverse

string = input("Enter a string: ")              
if is_palindrome(string):                       # Testing the function
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#3. Python program to check if a given number is an Armstrong number 
def is_armstrong(number):
    num_str = str(number)                                # Convert the number to a string to get its length
    num_digits = len(num_str)                           # Calculate the number of digits
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)           # Calculate the sum of each digit raised to the power of the number of digits
    
    return armstrong_sum == number                       # Check if the sum equals the original number
number = int(input("Enter a number: "))
if is_armstrong(number):                                # Test the function
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

#4. Python program to get the Fibonacci series between 0 to 50 
def fibonacci_series(limit):
    fib1, fib2 = 0, 1                                            # Initialize the first two Fibonacci numbers
    fibonacci_series = []                                       # Initialize an empty list to store the Fibonacci series
   
    while fib1 <= limit:                                                # Generate Fibonacci numbers up to the limit
        fibonacci_series.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2

    return fibonacci_series
fib_series = fibonacci_series(50)                                           # Call the function to get the Fibonacci series between 0 and 50

print("Fibonacci series between 0 and 50:")                                 # Print the Fibonacci series
print(fib_series)

#5. Python program to check the validity of password input by users
import re

def is_valid_password(password):
    
    min_length = 8                                                      # Define the criteria
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*()-+=]', password)
    
    # Check if all criteria are met
    if (len(password) >= min_length and                                 # Check if all criteria are met
        has_upper and has_lower and has_digit and has_special):
        return True
    else:
        return False


password = input("Enter your password: ")
if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password. Please make sure your password contains at least 8 characters, including uppercase and lowercase letters, digits, and special characters.")
