# Dictionaries
# All fun and games keep our crazy_x list... but we also need more information.  Introducing dictionaries!
# Dictionaries are defined using {} They are organised with keys that point to values, much like looking up something in a dictionary or information about a contact on our phones.
#Thus in our phone, the contact Filipe Paiva will hold lost of info for this entry. Could be phone number, work number, email, address and so on...

# Syntax
    # dict_name = {'example_key': 'value', 'example_key': 'value'}


# Defining a simple dictionary with two keys
dictionary_crazy_x = {
    'Carolina': 'she was actually nice',
    'Arthur': 'bit of a drinker'
}

print(dictionary_crazy_x)
print(type(dictionary_crazy_x))

# Accessing values - use the key!
print(dictionary_crazy_x['Carolina'])
print(dictionary_crazy_x['Arthur'])

# Adding a new key, pair value
dictionary_crazy_x['Kyle'] = 'Likes energy drinks :S'
print(dictionary_crazy_x)

dictionary_crazy_x['Kyle'] = 'Drinks energy drinks at 6am in the morning'
print(dictionary_crazy_x)

# Get out all of the keys
print(dictionary_crazy_x.keys())

# Get out all of the values
print(dictionary_crazy_x.values())

#