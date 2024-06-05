
#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd


#3. Write a Program to Convert Kilometers to Miles
#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.





#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

a = int(input("Enter a number: "))                    #input from the user

result = "Even" if a % 2 == 0 else "Odd"           # Using ternary operator to check if the number is even or odd

print(f"The number {a} is {result}.")                # Displaying the result

#2. Using input function take two number and then swap the number


x = int(input("Enter the first number: "))           #input from the user
y = int(input("Enter the second number: "))

# Swapping the numbers using a temporary variable
temp = x                                      # first number to temp
x = y                                         #second number to first number
y = temp                                      #temp to second number


print(f"After swapping, the first number is: {x}")      #Displaying the swapped numbers
print(f"After swapping, the second number is: {y}")     # Displaying the swapped numbers