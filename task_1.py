grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
#print(students_list)
students_sortlist = sorted(students_list)
#print(students_sortlist)
score_student = []
for i in range(len(grades)):
    s = sum(grades[i])/len(grades[i])
    #print(s)
    score_student.append(s)
#print(score_student)
score_students = dict(zip(students_sortlist, score_student))
print(score_students)
