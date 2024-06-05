#1. Python program to check leap year 

year = int(input("Enter a number: "))                            # user to enter the year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):     # If the year is divisible by 4 and not divisible by 100, or if it's divisible by 400, it's a leap year

    print(year, "is a leap year.")                               #Prints if the condition is satisfied
else:
    print(year, "is not a leap year.")                           #Prints if the condition is not satisfied




#2. Python Program to Find the Largest Among Three Numbers 

num1 = float(input("enter the first number:"))                  # user to enter FIRST numbers
num2 = float(input("Enter the second number: "))                # user to enter SECOND numbers
num3 = float(input("Enter the third number: "))                                           # user to enter THIRD numbers

# Check which number is the largest
if num1 >= num2 and num1 >= num3:                               
    largest = num1                                                                       # if the condition is satisfied number 1 is largest
elif num2 >= num1 and num2 >= num3:
    largest = num2                                                                       # if the condition is satisfied number 2 is largest
else:
    largest = num3                                                                       # if the condition is satisfied number 3 is largest

# Print the largest number
print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest)         # printing largest number



#3. Python Program to Check if a Number is Positive, Negative or 0 

number = float(input("Enter a number: "))                           # user to enter number
if number > 0:                                                     #checking if the number is greaterthan zero
    print("The number entered is positive.")
elif number < 0:                                                   #checking if the number is Lesserthan zero
    print("The number entered is negative.")
else:
    print("The number entered is zero.")                           # printing Zero

#4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical 
#Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders
#for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery 
#ased toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and
#the order amount and prints out the net amount that the customer is required to pay after the discount. #

product_code = int(input("Enter product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))   # Taking input from the user for product code and order amount
order_amount = float(input("Enter order amount in Rs.: "))                  # user to enter Amount
discount = 0                                                                # Initializing discount variable
if product_code == 1 and order_amount > 1000:                               # Checking conditions to determine discount based on product code and order amount
    discount = 0.1                                                          # 10% discount for battery-based toys if order amount is more than Rs. 1000
elif product_code == 2 and order_amount > 100:
    discount = 0.05                                                         # 5% discount for key-based toys if order amount is more than Rs. 100
elif product_code == 3 and order_amount > 500:
    discount = 0.1                                                          # 10% discount for electrical charging based toys if order amount is more than Rs. 500
discount_amount = discount * order_amount                                   # Calculating discount amount
net_amount = order_amount - discount_amount                                 # Calculating net amount to be paid after discount
print("Net amount to be paid after discount: Rs.", net_amount)              # Displaying the net amount to be paid after discount


#5. A transport company charges the fare according to following table: Distance Charges 1-50 8 Rs./Km 51-100 10 Rs./Km > 100 12 Rs/Km# Taking input from the user for distance traveled

distance = float(input("Enter the distance traveled in kilometers: "))
if distance <= 50:
    fare = distance * 8                                                           # Rs. 8 per kilometer for distances up to 50 km
elif distance <= 100:
    fare = distance * 10                                                          # Rs. 10 per kilometer for distances between 51 km and 100 km
else:
    fare = distance * 12                                                          # Rs. 12 per kilometer for distances greater than 100 km
print("The fare for traveling ",distance, "km is Rs.", fare)                      # Displaying the calculated fare
