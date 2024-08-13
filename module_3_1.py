import string

cals = 0


def caut_calls():
    global cals
    cals += 1


def string_info(input_string):
    caut_calls()
    return (len(input_string),
            input_string.upper(),
            input_string.lower())
def is_contains(input_string , list_to_search):
    caut_calls()
    input_string_lower = input_string.lower()
    return any(input_string_lower == item.lower()
               for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(cals)

