#1. Write a Python program to count the occurrences of each word in a given sentence
#string = “To change the overall look of your document. To change the look available in the gallery”

sentence = "To change the overall look of your document. To change the look available in the gallery"   # Given sentence


words = sentence.split()                            # Split the sentence into words


word_counts = {}                                    # Initialize an empty dictionary to store word counts


for word in words:                                  # Iterate through each word in the sentence 
    word = word.strip(".,!?")                       # Remove punctuation marks if any
    word = word.lower()                             # Convert the word to lowercase to ensure case-insensitive counting

    if word in word_counts:                         # Update the count of the word in the dictionary
        word_counts[word] += 1
    else:
        word_counts[word] = 1


for word, count in word_counts.items():             # Print the word counts
    print(f"'{word}': {count}")


#2. Write a Python program to remove a newline in Python
#String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"      # Given string
cleaned_string = string.replace("\n", "")               # Remove newline characters with an empty string
print(cleaned_string)                                   # Print the cleaned string


#3. Write a Python program to reverse words in a string
#String = “Deeptech Python Training”

string = "Deeptech Python Training"                     # Given string


words = string.split()                                  # Split the string into words


reversed_words = words[::-1]                            # Reverse the order of the words


reversed_string = ' '.join(reversed_words)              # Join the reversed words back into a string


print(reversed_string)                                  # Print the reversed string

#4. Write a Python program to count and display the vowels of a given text
#String=”Welcome to python Training”
# Given text
text = "Welcome to Python Training"                 # Given text


def count_and_display_vowels(text):                # Define a function to count and display vowels 
    vowels = 'aeiouAEIOU'                               # Define a string containing all vowels
    vowel_count = 0                                 # Initialize vowel count

    
    for char in text:                                # Iterate through each character in the text
        
        if char in vowels:                          # Check if the character is a vowel
            vowel_count += 1
            print(char, end=' ')

    
    print("\nTotal number of vowels:", vowel_count)         # Print the total count of vowels


count_and_display_vowels(text)                  # Call the function with the given text