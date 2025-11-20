# Lists and Loops: Exercise 4 (List Comprehension)

# Program Description: Generate a list which is a filter of the original list containing only words of length > 4 and starting with only vowels.

words = ["Apple", "egg", "Orange", "Sky", "umbrella", "Ink", "Ant"]
result = [word.lower() for word in words if len(word) > 4 and word[0].lower() in 'aeiou']
print(result)

# General Structure of List Comprehension:
# variable_name = [item iterable condition]