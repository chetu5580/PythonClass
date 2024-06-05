#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 

def display_file_content(filename):  
    file = open(filename, 'r')                          # Open the file for reading    
    for line in file:                                    # Iterate over each line in the file
        print(line.strip())                             # Strip removes any trailing newline characters 
    file.close()                                              # Close the file
display_file_content("python.prog/ABC.txt")


#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt” 
def count_words_in_file(file_name):
    
    with open(file_name, 'r') as file:                      # Open the file in read mode
      
        text = file.read()                                   # Read the entire content of the file
        
        words = text.split()                                 # Split the text into words based on whitespace
       
        word_count = len(words)                                  # Count the number of words
       
        print("Total number of words in the file:", word_count)      # Print the total number of words


count_words_in_file("python.prog/ABC.txt")              # Usage:

#3. Write a function in Python to count uppercase character in a text file “ABC.txt” 
def count_uppercase_in_file(file_name):
  
    uppercase_count = 0                                          # Initialize a variable to store the count of uppercase characters
    with open(file_name, 'r') as file:                              # Open the file in read mode
     
        for line in file:                                           # Iterate through each line in the file
           
            for char in line:                                         # Iterate through each character in the line
                
                if char.isupper():                                     # Check if the character is uppercase
                    
                    uppercase_count += 1                            # Increment the count if it's uppercase
   
    print("Total number of uppercase characters in the file:", uppercase_count)     # Print the total count of uppercase characters


count_uppercase_in_file("python.prog/ABC.txt")          # Usage:

#4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
def display_words(file_name):
    
    with open(file_name, 'r') as file:                              # Open the file in read mode
        
        for line in file:                                           # Iterate through each line in the file
            
            words = line.split()                                    # Split the line into words
            
            for word in words:                                      # Iterate through each word
                
                if len(word) < 4:                                       # Check if the word has less than 4 characters
                    
                    print(word)                                         # Display the word


display_words("python.prog/story.txt")                      # Usage: