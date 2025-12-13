# Functions: Exercise 3 (Using Data Structures with Functions)
# Program Description: Country-Cities
# This program lets a user pick a country and then store as many cities the user wants of that country in a dictionary.

def country_cities(country, cities):
    info = {}
    info[country] = cities
    return info

def main():
    while True:
        print("\nEnter the name of a Country and then its Cities.")
        print("Enter 'q' to quit at any time.")
        country_name = input("Enter Country Name: ").title()
        if country_name.lower() == 'q':
            break
        cities = []
        while True:
            city_name = input(f"Enter a city of {country_name}: ")
            if city_name != 'q':
                cities.append(city_name.title())
            else:
                print(country_cities(country_name, cities))
                break
        break

main()

