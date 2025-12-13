# Functions: Exercise 4 (Data Structures and Lambda functions with Functions)
# Program Description: Quote Dictionary Maker

def quote_matcher_dictionary(names, messages):
    quote_dictionary = dict(map(lambda name, message: (name, message), names, messages))
    return quote_dictionary

def main():
    people = []
    quotes = []
    while True:
        print("Enter the name of the Wise Person and the quote or Enter 'q' to quit.")
        name = input("Enter the name of the Wise Personality: ")
        if name.lower() == 'q':
            break
        quote = input("Enter the Quote: ")
        if quote.lower() == 'q':
            break
        else:
            people.append(name)
            quotes.append(quote)
    print(quote_matcher_dictionary(people, quotes))

main()

""" More concise version:

def main():
    quote_dictionary = {}
    while True:
        print("Enter the name of the Wise Person and the quote OR Enter 'q' to quit the program.")

        name = input("Enter the name of the Wise Personality: ")
        if name.lower() == 'q':
            break

        quote = input("Enter the Quote: ")
        if quote.lower() == 'q':
            break

        quote_dictionary[name] = quote
    print(quote_dictionary)
"""