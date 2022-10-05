# №1
# #a = int(input('a: '))
# #f = a // 100
# #s = (a // 10) % 10
# #l = a % 10
# #print('Последнее число: ', a % 10)
# #print('первое: ', a // 100)
# #print('вторая:', (a // 10) % 10)
# #print('сумма: ', f+s+l)
# №2
# # print('стоимость?')
# # r = int(input('Рублей: '))
# # k = int(input('Копейки: '))
# # n = int(input('Кол-во: '))
# # a = r * 100 + k
# # alm = a * n
# # print(f'С вас {alm // 100} и {alm % 100} копеек')
# # money = int(input('мои rubles: '))
# # sdacha = money * 100 - alm
# # print(f'Ваша сдача:  {sdacha // 100} руб. и {sdacha % 100} коп.')
# # #№3
# # a = int(input('a: '))
# # if a % 2 == 1:
# #     a = a + 1
# # else:
# #     a = a + 2
# # print(a)
# sec = int(input('sec: '))
# s = sec % 60
# m = sec // 60
# h = sec // 3600
# if m >= 60:
#     m = m - 60
#     h = h + 1
# if s < 10:
#     s = ': 0' + str(s)
# if m < 10:
#     m = ': 0' + str(m)
# if h < 10:
#     h = '0' + str(h)
# print(h, m, s)
# x = input('vvedi: ')
# temp = x[-1]
# print((x.index(temp)) + 1)
# print(len(x))
# name1 = 'artem'
# name2 = 'bambazaver'
# name3 = 'bibil'
#
# bratva = [name1, name2, name3]
# print(bratva)
# print(bratva[1][3:])
# path = 'C:/Python3/python.exe'
# print('Имя файла: ', path[11:])
# print('Расширение: ', path[-3:])
# print('Имя каталога: ', path[3:10])
# print('Полный путь к каталогу: ', path[:324])
# path = 'C:/Python3/python.exe'
# temp = path.split('/')
# print(temp)
# print('Имя файла: ', path[11:])
# print('Расширение: ', path[-3:])
# print('Имя каталога: ', path[3:10])
# print('Полный путь к каталогу: ', path[:324])
#
# chapter = input('Глава 1: ')
# page = input('Страница: ')
#
# chapter2 = input('Глава 2: ')
# page2 = input('Страница: ')
#
# chapter3 = input('Глава 3: ')
# page3 = input('Страница: ')
# print(chapter.ljust(15), page.rjust(15))
# print(chapter2.ljust(15), page2.rjust(15))
# print(chapter3.ljust(15), page3.rjust(15))
# x = "123456789"
# print(x[::2])
# print(x[::-1])
# print(x[::-2])
# x = "12'345'678"
# num = int(temp)
# print(num)
# temp = x.split("'")
# temp2 = temp[0] + temp[1] + temp[2]
# num = int(temp2)
# print(num)
# temp = x.replace("'", "")
# print(temp)
