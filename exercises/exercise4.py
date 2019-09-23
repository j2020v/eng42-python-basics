# Dictionary basics

# Define a dictionary called story1, it should have the following keys: start, Middle and End
story1 = {'start': 'In the beginning, there were plenty of animals',
          'middle': 'hurricane Gerald came and wiped out all the animals',
          'end': 'sadly, they all died.'
}

# Print the entire dictionary
print(story1)

# Print the type of your dictionary
print(type(story1))

# Print only the keys
print(story1['start'])
print(story1['middle'])
print(story1['end'])

# Print only the values
print(story1.values())

# Now let's add a new key: value pair
    # 'hero': yoursuperhero

story1['Hero'] = 'hurricane Gerald'
print(story1)
