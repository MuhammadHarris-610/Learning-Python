# Conditionals: Exercise 5 (Conditionals with Loops)

# Program Description: Validating Usernames

current_users = ['Taha', 'Abdul Hadi', 'Osaid', 'Abdullah', 'Ibrahim']
lower_current_users = [name.lower() for name in current_users]
new_users = ['Nooh', 'Ibrahim', 'Taha', 'Moosa', 'Esa']

for user in new_users:
   if user.lower() in lower_current_users:
      print('Username already taken; enter a new username.')
   else:
      print('Username is available.')