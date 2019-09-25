# Functions and Functional programing
# functions are like machines. They take in arguments and they have a block of code to run. They output (return) something (optional).
# Running and calling a function
# They need to be called to be executed

# Good practices:
#   good names
#   lower case and separated with an _ (underscore)
#   should be atomic and small - makes them testable, reduces technical debt
#   comments when appropriate
#   functions allow us to be DRY - DON'T REPEAT YOURSELF
#   do NOT print in functions  -- RETURN

## CLEANER, DRIER AND TESTABLE

#separation of concerns

def return_hey_to_zeus():
    return('hey Zeus')

def full_name(f_name,l_name):
    full = f_name + ' ' + l_name
    return 'filipe'

print(return_hey_to_zeus())
print(full_name('Abror', 'Ilkhamov')) #Arguments are not optional here

# This is the basis of all tests
# Assertion (check for expected outcomes)
# Feedback output to our users
print(full_name('Abror', 'Eddi')) == 'Abror Eddi'