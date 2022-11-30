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
calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"
for i in range(7):
    calText += DAYS[i]
print(calText)
weeksep = ("+----------" * 7) + "\n"
blankrow = ("          " * 7) + "|\n"
currentdate =  datetime.date(year, month, 1)
while currentdate.weekday() != 0:
    currentdate -= datetime.timedelta(days=1)
while True:
    calText += weeksep
    daynumberow =  ""
    for i in range(7):
        daynumberlabel = str(currentdate.day).rjust(2)
        daynumberow += "|" + daynumberlable + (" " * 8)
        currentdate += datetime.timedelta(days=1)
    calText += "|\n"
    calText += daynumberow
    for i in range(3):
        calText += blankrow
    if currentdate.month != month:
        break
calText += weeksep
print(calText)
FileName = "calendar_{}_{}.txt".format(month,year)
with open(FileName, "w") as file:
    file.write(calText)
print("сохранено в" + FileName)
