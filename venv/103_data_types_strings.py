# String
# These are a list of characters put together, defind by '' or ""

my_string = 'Amazing Grilled Fish'
print(type(my_string))
# You can print it
print(my_string)

# Joining of strings = concatenation
first_name = 'Boris'
last_name = 'Becker'

full_name = first_name, last_name
print(first_name, last_name)

# Concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)

# Interpolation
name = 'Rachel'
welcome_message = 'Hey there, how you doin?'
print(f'Hey there, {name} how you doin?')
# place f in the beginning of the string then use {} to interpolate python variables inside


# Useful methods for strings
my_string = ' Hello this is an amazing string      '

#count()
print(my_string.count('i'))

#.strip() -- removes trailing white spaces
print(my_string.strip())

#len() -- not a method -- general method built in; counts the characters
print(len(my_string))

#.lower()
print(my_string.lower())

#.upper()
print(my_string.upper())

#.capitalize()
print(my_string.strip().capitalize())

#.replace(arg_int, arg_two)
print(my_string.replace('an', 'THE'))

#.split(arg) -- list
print(type(my_string.split(' ')))

