'''
Let say you are a teacher and you have different student records containing id of a student and the marks list in each subject where
different students have taken different number of subjects. All these records are in hard copy. You want to enter all the data in computer
and want to compute the average marks of each student and display
'''


def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        studentMarks = input("Enter student's marks separated by comma: ")
        moreStudents = input("Do you have more students?")

        if studentId in D:
            print(studentId, "is already inserted")

        else:
            D[studentId] = studentMarks.split(",")

        if moreStudents.lower().strip() == "no":
            return D



studentData = getDataFromUser()
print(studentData)


def getAvrMarks(D):
    avrgMarksDict = {}
    for x in D:
        sum = 0
        L = D[x]
        for marks in L:
            sum += int(marks)
            avrgMarksDict[x] = sum/len(L)
    return avrgMarksDict


avgMarks = getAvrMarks(studentData)
print(avgMarks)