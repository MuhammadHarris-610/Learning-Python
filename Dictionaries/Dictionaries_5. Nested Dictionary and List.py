# Dictionaries: Exercise 5 (Nested Dictionaries and Lists)

# Program Description: Countries and Historic Cities

countries = {
   'Saudi Arabia': ['Mecca', 'Medina', 'Taif'],
   'Syria': ['Damascus', 'Aleppo', 'Homs'],
   'Iraq': ['Babylon', 'Baghdad', 'Kufa', 'Basra'],
   'Palestine': ['Jerusalem', 'Hebron', 'Bethlehem', 'Nablus', 'Jericho'],
   'Turkiye': ['Constantinople', 'Antioch'],
}

for country, cities in countries.items():
   print(f"Country: {country}\nCities: {cities}\n")


