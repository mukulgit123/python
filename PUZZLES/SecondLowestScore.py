# Custom Input for the test which was failing and the addition of lines from 12- 15 helped to solve the same
# 5
# Mike
# 19
# Tike
# 19
# Rike
# 20
# Like
# 20
# Fike
# 21
if __name__ == '__main__':
    students = []  # Created students array
    student_count = int(input())  # Entered the count of students
    if student_count > 5 and student_count < 2:  # Constraint for number of students
        exit()
    for _ in range(student_count):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    lowest = min(students, key=lambda x: x[1])
    mins = [x for x in students if x[1] == lowest[1]]
    for x in mins:
        students.remove(x)
    # print(students)
    # print(students) - Printed students here as the test case where the
    # lowest occurred more than once failed
    secondLowest = min(students, key=lambda x: x[1])
    secondLowestList = sorted(
        [x[0] for x in students if x[1] == secondLowest[1]])
    for student in secondLowestList:
        print(student)
    #assumedLowest = 10000
    #lowest = [ x for x in students if x[1] < assumedLowest ]
    # print(lowest)
    # print(students)
