# # # # # x = 7
# # # # # if x <= 7:
# # # # #     print('menshe ili ravno')
# # # # # else:
# # # # #     print('bolshe')
# # # # # print(x == 7)
# # # # #
# # # # #
# # # # #
# # # # # x = int(input('Введите число: '))
# # # # # if x < 0:
# # # # #     print('Отрицательное')
# # # # # elif x > 0:
# # # # #     print('Положительное')
# # # # # else:
# # # # #     print('Ноль')
# # # # #
# # # # #
# # # # #
# # # # # y = int(input('Введите год: '))
# # # # # if y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
# # # # #     print('Високосный')
# # # # # else:
# # # # #     print('Не весокосный')
# # # # #n1 = int(input('Первое число: '))
# # # # # oper = input('Введи операцию (+, -, *, /): ')
# # # # # n2 = int(input('Второе число: '))
# # # # # lst = ["+", "-", "*", "/"] #cписок
# # # # # #if oper in lst: #если операция есть в списке то
# # # # #     if oper == '+': #если операция равна слову(символу) из списка, то использовать его
# # # # #         print(n1 + n2)
# # # # #     if oper == '*':
# # # # #         print(n1 * n2)
# # # # #     if oper == '-':
# # # # #         print(n1 - n2)
# # # # #     if oper == '/':
# # # # #         print(n1 / n2)
# # # # # #else:
# # # # #     print('Написал фигню')
# # # # # n1 = int(input('Первое число: '))
# # # # # n2 = int(input('Второе число: '))
# # # # # n3 = int(input('Третье число: '))
# # # # # countp = 0
# # # # # counto = 0
# # # # #
# # # # # if n1 > 0:
# # # # #     countp += 1
# # # # # elif n1 < 0:
# # # # #     counto += 1
# # # # #
# # # # # if n2 > 0:
# # # # #     countp += 1
# # # # # elif n2 < 0:
# # # # #     counto += 1
# # # # #
# # # # # if n3 > 0:
# # # # #     countp += 1
# # # # # elif n3 < 0:
# # # # #     counto += 1
# # # # # print('Положительных: ', countp)
# # # # # print('Отрицательных: ', counto)
# # # # n1 = int(input('Первое число: '))
# # # # n2 = int(input('Второе число: '))
# # # # n3 = int(input('Третье число: '))
# # # # lst =[n1, n2, n3]
# # # # max = max(lst)
# # # # min = min(lst)
# # # # print('Наибольшее:',max)
# # # # print('Наименьшее:', min)
# # # h = int(input("Часы: "))
# # # m = int(input("Минуты: "))
# # # s = int(input("Секунды: "))
# # #
# # # if h > 23 or h < 0:
# # #     print('ne pravda')
# # # elif m > 59 or h < 0:
# # #     print('ne pravda')
# # # if s > 59 or h < 0:
# # #     print('ne pravda')
# # # else:
# # #     print('narmalna')
# # # print(f"{h}:{m}:{s}")
# # tick = input('Введите номер билета (6 цифр): ')
# # if len(tick) == 6 and tick.isdigit():
# #     first = tick[:3]
# #     last  = tick[-3:]
# #     summa = int(first[0] + first[1] + first[2])
# #     summa2 = int(last[0] + last[1] + last[2])
# #     if summa == summa2:
# #         print("kaef")
# #     else:
# #         print('ne povezlo')
# # else:
# #     print('ne to')
# m = input("Номер месяца: ")
# if m.isdigit() and 12 >= int(m) >= 1:
#     m = int(m)
#     if 3 <= m <= 5:
#         print('vesna kaef')
#     if 6 <= m <= 8:
#         print('leto kaef')
#     if 9 <= m <= 11:
#         print('ocen ne kaef')
#     if 12 <= m <= 2:
#         print('zima ne kaef')
#     else
hamsters = int(input('кол-во: '))
if 11 <= hamsters <= 19:
    print(hamsters, "hamsters")
elif hamsters & 10 == 1:
    print(hamsters, "hamster")
elif 2 <= hamsters <= 4:
    print(hamsters, "homyaka")
else:
    print(hamsters, "homyakov")
