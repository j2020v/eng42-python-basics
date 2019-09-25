cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford', 'Corvette']

#Syntax

# for <placeholder> in <iteratable>:
    # block of code
    # indented gets run every iteration
    # don't forget the colon

# for car in cars:
#     print('hey')
#     print(car)
#
#
# embeded_list = [['Filipe', 'Francis'],['Mustafa', 'David', 'Jillian']]
# for data in embeded_list:
#     print(data)

#     for name in data:
#         print(name.upper())

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'complete modules': ['sword', 'augmented senses', 'no face', 'no name']
}

count_1 = 1
for key in student1:
    print(f'{count_1}. {key}: {student1[key]}')
    count_1 += 1

for key, values in student1.items():
    print(count_1, key, values)
    count_1 += 1
#
students = {
    'student1': student1,
    'student2': {
        'name': 'Stirling Archer',
        'stream': 'Chaos',
        'grade': 10,
        'module': ['danger', 'robust liver']


#Task two: do the same but with the embedded dictionary
for student_key in students:
    print(student_key)
        count_1 += 1,
        for key in students[student_key]:
            print(count_1, key, ':',   students[student_key][key])
            count_1 += 1,

    for key1 in students:
        print(key1)
        print (type(students[key1]))
    for key2 in students[key1]:
        print (key2)
        print (students[key1][key2])
        print(f'{count_1} - {key2}, {students [key1][key2]}')