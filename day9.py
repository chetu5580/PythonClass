#1. Write a Python program to Count all letters, digits, and special symbols from the given 
#string Input = “P@#yn26at^&i5ve” 
#Output: Chars = 8 Digits = 2 Symbol = 3 
def count_characters(string):
                                              
    letter_count = 0                               # Initialize counts for letters                                      
    digit_count = 0                                # Initialize counts for digits
    symbol_count = 0                               # Initialize counts for symbols
      
    for char in string:                                      # Iterate through each character in the string
        
        if char.isalpha():                                          # Check if the character is a letter
            letter_count += 1
        elif char.isdigit():                                                # Check if the character is a digit
            digit_count += 1
        else:
            symbol_count += 1                                                  # If it's not a letter or digit, it's considered a symbol
    
    print("Chars =", letter_count, "Digits =", digit_count, "Symbols =", symbol_count)           # Print the counts

input_string = "P@#yn26at^&i5ve"                                            # Test the function with the given input
count_characters(input_string)

#2. Write a Python program to remove duplicate characters of a given string. 
#Input = “String and String Function” 
#Output: String and Function 

def remove_duplicates(string): 
    result = ""                                                                              # Initialize an empty string to store the result
    seen = set()                                                     # Initialize a set to keep track of encountered characters
    for char in string:                                             # Iterate through each character in the string
        if char not in seen:                                            # Add the character to the result if it hasn't been encountered before
            result += char
            seen.add(char)
    return result
input_string = "String and String Function"                             # Test the function with the given input
output_string = remove_duplicates(input_string)
print("Output:", output_string)

#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
#Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 
def count_characters(string):
    
    uppercase_count = 0                                                         # Initialize counts for uppercase
    lowercase_count = 0             # Initialize counts for lowercase
    numeric_count = 0               # Initialize counts for  numeric values
    special_count = 0               # Initialize counts for  special characters
     
    for char in string:                             # Iterate through each character in the string
       
        if char.isupper():                          # Check if the character is uppercase
            uppercase_count += 1 
        elif char.islower():                        # Check if the character is lowercase
            lowercase_count += 1
        elif char.isdigit():                            # Check if the character is a digit
            numeric_count += 1
        else:
            special_count += 1                       # If it's not uppercase, lowercase, or a digit, it's considered a special character
    
    print("UpperCase:", uppercase_count, "LowerCase:", lowercase_count, "NumberCase:", numeric_count, "SpecialCase:", special_count)         # Print the counts

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"                # Test the function with the given input
count_characters(input_string)


#4. Write a Python Count vowels in a string 
#input= “Welcome to Python Assignment” 
#Output: Total vowels are: 8
def count_vowels(string):
    
    vowels = {'a', 'e', 'i', 'o', 'u'}              # Define a set of vowels
    vowel_count = 0                                     # Initialize a count for vowels
      
    for char in string:                                               # Iterate through each character in the string
        if char.lower() in vowels:                       # Check if the character is a vowel (case insensitive)
            vowel_count += 1
    
    return vowel_count

input_string = "Welcome to Python Assignment"           # Test the function with the given input
vowel_count = count_vowels(input_string)
print("Total vowels are:", vowel_count)                 # Print the count of vowels
