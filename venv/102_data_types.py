# Numerical Data Types
# -Ints, long, float, complex
# These are numerical data types which we can use numerical operators

# Complex and long we don't use as much
# Complex bring an imaginary type of number
# long - are integers of unlimited size


# int - stands for integers
# Whole numbers
my_int = 10
print(my_int)
print(type(my_int))

#Operator - add, subtract, divide, multiply and exponential
print(4 + 3)
print(5 - 1)
print(4/2) # Divisions automatically get converted to float
print(4//2) #Double divide drops the float
print(4*2)
print(3**2)

#Modulus finds out the remainder
print(10%3)
print(22%3)

# Comparison operators
# = - Assignment
# == - Equal to
# < / > - Greater and less than
# <= - Less than or equal to
# >= - Greater than or equal to
# != - Not equal to
# is / is not

my_variable1 = 10
my_variable2 = 13

print(my_variable1 == my_variable2)
print(my_variable2 > my_variable1)

# Boolean Values
# Defined by either True or False
print(type(True))
print(type(False))
print(0 == False)
print(1 == True)

# None
print(None)
print(type(None))

# Logical AND & OR
a = True
b = False

# Using *and* both sides have to be true for it to result in true
print(a and True)
print ((1 == 1) and True)

# Use or, ONLY 1 side needs to be true
print('this will print true')
print (True or False)
print(True or 1 ==2)