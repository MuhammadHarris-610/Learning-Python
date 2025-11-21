# User Input and While Loops: Exercise 6 (User Input, While Loop and Dictionary)
# Program Description: Dream place to visit

sites = {}
active = True
while active:
   name = input("Enter name: ")
   site = input("Enter the Place you want to visit the most: ")
   sites[name] = site
   repeat = input("Would you let another person respond? (yes/no) ")
   if repeat == 'no':
      active = False

for name, site in sites.items():
   print(f"{name.title()} wants to visit {site.title()}.")