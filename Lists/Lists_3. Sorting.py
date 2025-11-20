# Lists: Exercise 3 (Sorting a List)

# Program Description: Holy Sites
locations = ['Mecca', 'Jerusalem', 'Damascus', 'Medina', 'Hebron', 'Basra', 'Kufa']
print(f'Original List: {locations}')

print(f'\nSorted List: {sorted(locations)}') # Used to create a temporary sorted copy of a list.
print(f'\nOriginal List again: {locations}')

print(f'\nReverse Sorted List: {sorted(locations, reverse=True)}') # Created a temporary sorted copy of the list, but in reverse order.
print(f'\nOriginal List again: {locations}')

locations.reverse()
print(f'\nReversed Original List: {locations}') # Reversed the order of list permenantly.

locations.reverse()
print(f'\nList Reversed Back: {locations}')

locations.sort()
print(f'\nSorted Original List: {locations}') # Sorted the List permenantly

locations.sort(reverse=True)
print(f'\nSorted Original List in Reverse: {locations}') # Sorted the List permenantly in reverse order