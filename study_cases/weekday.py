def get_weekday(number):
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье",
    }
    if number not in days:
        raise ValueError("невалидные данные")
    return days[number]


if __name__ == "__main__":
    day_number = input("Введите номер дня недели: ")
    print(get_weekday(int(day_number)))
