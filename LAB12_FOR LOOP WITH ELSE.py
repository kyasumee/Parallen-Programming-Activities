#PROGRAM TO DISPLAY STUDENT'S MARKS FROM RECORD
student_name = 'Soyuj'

marks = {'James': 90, 'Jules':55, 'Arthur':77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')