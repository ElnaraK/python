N = int(input())
students = []
grades = []
for i in range(N):
    n = input()
    g = float(input())
    students.append([n,g])
    grades.append(g)
c = min(grades)
while min(grades)==c:
    grades.remove(c)
second = min(grades)
for n, g in sorted(students):
    if g == second:
        print(n)
