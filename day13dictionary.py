# 1. Write a Python program and calculate the mean of the below dictionary. 

#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

#Output: 6.2 

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}        # Define the dictionary
mean_value = sum(test_dict.values()) / len(test_dict)           # Calculate the mean
print("The mean is:", mean_value)           # Print the result


#2.Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary : 

#dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

dic1 = {1: 10, 2: 20}                   # Define the dictionaries
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {**dic1, **dic2, **dic3}         # Create a new dictionary by concatenating the above dictionaries

print("Concatenated dictionary:", new_dict)     # Print the result

#3.Write a Python program to get the key, value and item in a dictionary. 

#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}           # Define the dictionary


for key, value in dict_num.items():                             # Iterate through the dictionary and print key, value, and item
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")