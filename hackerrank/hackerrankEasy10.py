N = int(input())
students = []
student_marks = {}
for i in range(N):
    student = list(map(str, input().split(maxsplit=4)))
    students.append(student)
    scores = float(student[1])+float(student[2])+float(student[3])
    student_marks[student[0]] = scores/3
S = input()
print('%.2f' %student_marks[S])