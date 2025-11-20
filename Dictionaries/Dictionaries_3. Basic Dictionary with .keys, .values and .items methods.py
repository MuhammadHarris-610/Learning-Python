# Dictionaries: Exercise 3 (Basic Dictionary)

# Program Description: Language Poll

people = ['Harris', 'Abdul Hadi', 'Taha', 'Abdullah', 'Osaid', 'Ibrahim']
people_lower = [name.lower() for name in people]

fav_lang = {
   'harris': 'Arabic',
   'taha': 'Pashto',
   'osaid': 'Turkish'
}

for name in people_lower:
   if name in fav_lang:
      print(f"I see {name.title()} you like {fav_lang.get(name)}")
   else:
      print(f"{name.title()} kindly take the poll.")

# .keys method returns keys of the dictionary in the form of a view object.
# .values method returns values of the dictionary in the form of a view object.
# .items method returns key-value pairs of the dictionary in the form of a view object.