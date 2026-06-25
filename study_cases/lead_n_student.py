class Lead:
    def __init__(self, name):
        self.name = name


def change_name(lead, new_name):
    lead.name = new_name


# ________ Визуальное разделение классов ________
class Student:
    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades


def get_avg_grades(student):
    if not student.grades:
        return 0
    return sum(student.grades) / len(student.grades)


# ______ Проверки _______
if __name__ == "__main__":
    lead = Lead("Олег")
    print("Изначальное имя: " + lead.name)
    change_name(lead, "Дмитрий")
    print("Имя после изменения функцией: " + lead.name)

    students = [
        Student("Анна", 20, [4.5, 5.0, 3.5]),
        Student("Борис", 22, [3.0, 4.0, 5.0]),
        Student("Вера", 19, [5.0, 5.0, 4.0]),
    ]
    for student in students:
        print(f"{student.name}: средний балл {get_avg_grades(student):.2f}")

    print("Студенты со средним баллом выше 4.1: ")
    for student in students:
        top_students = []
        avg = get_avg_grades(student)
        if avg > 4.1:
            top_students.append(student)
            print(top_students)
