#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 
def div(x, y):                                          #funtion for division
    return x / y
num1 = 10                                               # Initializing 10 to num1
num2 = 5                                                # Initializing 5 to num2
result = div(num1, num2)                                # Call the function and pass two numbers and storing in result
print("Division:", result)                              # Display the division result

#2. Declare a square() function with one parameter. Then call the function and pass one number and display the square of that number .
def square(x):                                          #funtion for square
    return x * x

number = 5                                              #Initializing 5 to number
result = square(number)                                 # Call the function and pass the numbers and storing in result
print("Square:", result)                                # Display the square of the number


#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
def maxi(numbers):                                      # funtion for maximum
    maximum_value = numbers[0]                          # Initialize maximum_value with the first element of the list
    for num in numbers:
        if num > maximum_value:
           maximum_value = num
    return maximum_value                                #returning Maximum value

def mini(numbers):
    minimum_value = numbers[0]                          # Initialize minimum_value with the first element of the list
    for num in numbers:
        if num < minimum_value:
            minimum_value = num
    return minimum_value                                #returning Manimum value


numbers = [23, 56, 12, 45, 78]
print("Numbers:", numbers)

max_number = maxi(numbers)                             #function call
min_number = mini(numbers)                             #function call
print("Maximum number:", max_number)                   # Display the  Maximum value
print("Minimum number:", min_number)                   # Display the Manimum value

#4. Accept a name from the user and display that in lower case using lower() function

def lowercase_name(input_name):                       #function to display name into lowercase
    return input_name.lower()

name = input("Enter your name: ")                     #user input name

lowercase_name = lowercase_name(name)                 #fuction call to Convert the name to lowercase 
print("Name in lowercase:", lowercase_name)          # Display the name in lowercase