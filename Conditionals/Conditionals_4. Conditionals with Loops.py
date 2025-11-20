# Conditionals: Exercise 4 (Conditionals with Loops)

# Program Description: Greeting Users

usernames = []
if usernames: # Checks whether the list is empty or not.
   for username in usernames:
      if username == 'Admin':
         print(f'Assalam-u-Aleykum wa Rahmatullah {username}')
      else:
         print(f'Assalam-u-Aleykum {username}')
else:
   print('We need to find some users!')