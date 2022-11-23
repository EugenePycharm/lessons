import random as r
import datetime

while True:
    days = input('сколька: ')
    if not days.isdigit() or int(days) > 70 or int(days) < 2:
        print("не смешно")
        print("=" * 20)
    else:
        days = int(days)
        break
birthdays = []
startofyear = datetime.date(2022, 1, 1)
for _ in range(days):
    shift = r.randint(0, 364)
    shfitofdays = datetime.timedelta(shift)
    birthday = startofyear + shfitofdays
    birthdays.append(birthday)
for index in range(days):
    print(f"{index + 1} {birthdays[index]}")
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раз")
