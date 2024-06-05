#1. Calculate the multiplication and sum of two numbers

x = 10                                                 #declareing 10 
y= 20                                                  #declareing 20 
mul=x*y                                                # multiply 2 numbers
sum=x+y                                                # sum 2 numbers
print(mul)                                             #printing multiplied value of 2 numbers
print(sum)                                             #printing multiplied value of 2 numbers

#2. Declare two variables and print that which variable is largest using ternary
#operators
z=True if y>x else False                               #ternary oparator
print(z)                                               # result printing



#3. Python program to convert the temperature in degree centigrade to Fahrenheit

a=40                                                    # degree  centigrade declaration
b=(a*9/5)+32    # converting degree centigrade to Fahrenheit
print(b)        #  printing Fahrenheit


#4. Python program to find the area of a triangle whose sides are given
m=3                         #side 1 of triangle
n=4                         #side 2 of triangle
o=5                         #side 3 of triangle

t=(m+n+o)/2                          # calculating semi perimeter
area = (t*(t-m)*(t-n)*(t-o)) **0.5   # calculating area
print(area)                          #area printing