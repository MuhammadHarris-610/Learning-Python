# Lists: Exercise 1 (Working with indices)

# Basic Index Operations
names = ['Taha', 'Abdul Hadi', 'Osaid', 'Abdullah', 'Ibrahim']
print(f'Assalam-u-Aleykum {(names[0])}')
print(f'Sub-a-Khair {(names[1])}')
print(f'Gunaydin {(names[2])}')
print(f'Hos Geldin {(names[3])}')
print(f'Selmaun Aleykum {(names[4])}')

# Using basic methods on lists
names.append('Harris') # Used to add a value to the end of a list.
print(f'Merhaba {names[-1]}')

names.insert(3, 'Ilyas') # Used to Insert a value at a particular position in a list.
print(f'Hayirli Sabahlar {names[3]}')
print(names)

not_friend = names.pop() # Used to remove or cut/paste a value from a list/ from a list to another list.
print(f'{not_friend} is not my friend anymore.')
print(names)

imaginary_friend = 'Ilyas'
names.remove(imaginary_friend) # Used to remove a value from a list.
print(f'{imaginary_friend} was my iota friend.')
print(names)