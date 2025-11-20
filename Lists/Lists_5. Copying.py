# Lists: Exercise 5 (Copying)

# Program Description: Favorite Foods
my_foods = ['Biryani', 'Karahi', 'Paaye']
friend_foods = my_foods[:] # Created a permenant copy of the original list with the only difference being the identifier.
my_foods.append('Nehaari')
friend_foods.append('Pulao')
print(f'My favorite foods are {my_foods}')
print(f"My friend's favorite foods are {friend_foods}")