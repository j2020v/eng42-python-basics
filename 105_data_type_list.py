# Lists
# Lists keep object in order of index, it's defined by []

# Example of a list - index
crazy_x_partners = ['Carolina', 'JSON', 'Arthur', 'Lana!']

# print(crazy_x_partners) -- READ ALL
print(crazy_x_partners)
print(type(crazy_x_partners))

# Get a particular record out -- READ ONE
print(crazy_x_partners[0]) #place index inside the square brackets

# How do I print the last one?
print(crazy_x_partners[-1])

# Maybe we want to change a record in a specific index?
# Re-assign an index
print(crazy_x_partners[3])
crazy_x_partners[3] = 'LANAAA!! DANGER ZONE!!'
print(crazy_x_partners[3])

# Add more people to the list -- CREATE ONE append()
print(crazy_x_partners)
crazy_x_partners.append('Cyral Figus')
print(crazy_x_partners)

# Insert in index in a specific location
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)

# Remove someone form the list -- DESTROY ONE
crazy_x_partners.remove('JSON')
print(crazy_x_partners)

crazy_x_partners.pop # Removes the last index
print(crazy_x_partners)

crazy_x_partners.pop(1) #Removes based on the index
print(crazy_x_partners)

# Mixed data and lists
# Lists can have many data types
hybrid_list = ['this is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]


# What happens when you have 300000000 index?
# -- Loops and other data formats

# Tuples are immutable lists -- do not change
my_tuple = (2, 'hello', 22, 'more value')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
