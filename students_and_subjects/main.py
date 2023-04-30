students = {}


def add_student():
    name_student = input("Введите имя ученика: ")
    subjects = input("Введите предметы, которые он изучает (через пробел): ").split()
    students[name_student] = subjects


def show_all():
    sorted_students = sorted(students.items(), key=lambda x: x[0], reverse=True)
    for name_student, subjects in sorted_students:
        print(name_student + ": " + ", ".join(subjects))


def student_for_sub(subject):
    result = []
    for name_student, subjects in students.items():
        if subject in subjects:
            result.append(name_student)
    return result


def sub_for_students(name_student):
    if name_student in students:
        return students[name_student]
    else:
        return []


n = int(input("Введите количество учеников: "))
for i in range(n):
    add_student()

show_all()

subject = input("Введите предмет: ")
students_for_subject = student_for_sub(subject)
print("Ученики, изучающие предмет " + subject + ": " + ", ".join(students_for_subject))

name = input("Введите имя ученика: ")
subjects_for_student = sub_for_students(name)
print("Ученик " + name + " изучает предметы: " + ", ".join(subjects_for_student))
