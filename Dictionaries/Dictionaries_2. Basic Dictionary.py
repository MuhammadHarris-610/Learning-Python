# Dictionaries: Exercise 2 (Basic Dictionary)

# Program Description: Major Rivers

rivers = {
   'Nile': 'Egypt',
   'Amazon': 'Brazil',
   'Mississippi': 'USA',
   'Yellow': 'China',
   'Indus': 'Pakistan',
   'Euphrates': 'Syria',
   'Tigris': 'Iraq',
}

for river, country in rivers.items():
   print(f"The {river} runs through {country}")