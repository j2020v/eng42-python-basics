# Nest lists and dictionaries

# nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice', {'name': 'Buttercup'}]]

# variable_bread = nested_list[0]
# variable_bread = nested_list[2]
# print(variable_bread)

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'complete modules': ['sword', 'augmented senses', 'no face', 'no name']
}

students = {
    'student1': student1,
    'student2': {
        'name': 'Stirling Archer',
        'stream': 'Chaos',
        'grade': 10,
        'module': ['danger', 'robust liver']
    }
}

print(students['student1']['name'])