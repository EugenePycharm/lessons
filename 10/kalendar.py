import datetime

MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
while True:
    year = input("Год: ")
    if year.isdigit() and int(year) > 0:
        break
while True:
    month = input("Месяц: ")
    if month.isdigit() and int(month) > 0:
        break
calText = ""
calText += (" " * 34) + MONTHS(month - 1) + " " + str(year)
for i in range(7):
    calText += DAYS[i]
