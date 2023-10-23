# Author: caleb moura

# Use the find method to return index of the first "t"
word = "flibbertigibbet"
t_index = word.find("t")

# Print the letter immediately after the first "t"
following_letter = word[t_index + 1]

# Create variable storing my first name in lowercase
first_name = "caleb"

# Print first name in uppercase using string method
upper_case_name = first_name.upper()

# Use split method to split the sentence at each comma
sentence = "I wish, I wish, I was a fish."
split_sentence = sentence.split(",")

# Print results
print(f"The index of the first 't' is: {t_index}")
print(f"The letter immediately following the first 't' is: {following_letter}")
print(f"My first name in uppercase is: {upper_case_name}")
print(f"The split sentence is: {split_sentence}")