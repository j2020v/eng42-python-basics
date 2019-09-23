# Variable in Python
# Variables is a box. You can give it a name and put stuff inside

#Assigning a Variable
# Giving box a name and putting stuff inside
box_variable = 'Books and stuff'

# Looking inside the box
print('box_variable')

#Re Assinging a Variable
# Variables are mutable - Hence they can change/be re-assigned
box_variable = "CD's and other stuff"
print(box_variable)

#Re Assigning Variable with an integer
# Variables can hold any data type inside
box_variable = 14
print(box_variable)

# Important python function
# print(arguments)
print(box_variable) # printing string
print('Hello', box_variable) #overloading with two arguments

# type()
# output the data type of an object
print(type('hello'))
print(type(14))
print(type(14.0))

variable_number = '14'
# print (type('10'*variable_number)) THIS WILL BREAK -- DATATYPES ARE KEY --

# input ()
#it prompts user for input
print('What is your favorite color?')
user_response = input('Now really, what is your favorite color?')
print(user_response)