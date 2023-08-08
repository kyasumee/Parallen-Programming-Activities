name = input("Name of Student: ")
prelim = input("Prelim Exam: ")
midterm = input("Midterm Exam: ")
final = input("Final Exam: ")
project = input("Project: ")
attendance = input("Attendance: ")

perEqui = float(prelim) * 0.15 + float(midterm) * 0.20 + float(final) * 0.30 + float(project) * 0.20 + float(attendance) * 0.15
print ("Percentage Equivalent: " + str(perEqui))

if perEqui >= 98 or perEqui == 100:
    print("Grade: 1.00")
    print("Excellent")

elif perEqui >= 95 or perEqui == 98:
    print("Grade: 1.25")
    print("Very Satisfactory")
    
elif perEqui >= 92 or perEqui == 94:
    print("Grade: 1.50")
    print("Satisfactory")

elif perEqui >= 89 or perEqui == 91:
    print("Grade: 1.75")
    print("Fairly Satisfactory")

elif perEqui >= 86 or perEqui == 88:
    print("Grade: 2.00")
    print("Good")
    
elif perEqui >= 83 or perEqui == 85:
    print("Grade: 2.25")
    print("Fairly Good")

elif perEqui >= 80 or perEqui == 82:
    print("Grade: 2.50")
    print("Fair")

elif perEqui >= 77 or perEqui == 79:
    print("Grade: 2.75")
    print("Below Fair")
    
elif perEqui >= 75 or perEqui == 76:
    print("Grade: 3.00")
    print("Passed")

elif perEqui <=74:
    print("Grade: 5.00")
    print("Failed")
    
else:
    print("INC")
    print("Requirements not fully met")