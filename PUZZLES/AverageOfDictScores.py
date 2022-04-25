# Sample input looks as below
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        if len(scores) == 3:
            student_marks[name] = scores
        else:
            exit()
        for i in scores:
            if i < 0 or i > 100:
                exit()
        if n < 2 or n > 5:
            exit()
    query_name = input()
    for student in student_marks:
        if student == query_name:
            print("{:.2f}".format(
                sum(student_marks[student]) / len(student_marks[student])))
