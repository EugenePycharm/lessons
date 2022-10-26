# ZeroDivisionError: division by zero
# x = 7/0
#
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# x = 7 + 'adam'
#
# SyntaxError: unterminated string literal
# x = 'Привет я артем
#
# ValueError: invalid literal for int() with base 10: 'artem'
# int('artem')
#
# NameError: name 'x' is not defined
# print(x)
#
# No such file.txt or directory: 'summa'
# open(file.txt='summa')
#
# def summa(numbers):
#     return sum(numbers)
#
#
# assert summa([1, 2]) == 3
# try:
#    div = int(input('Введи число для деления: '))
#    x = 5 / div
# except ZeroDivisionError:
#     print('Не дели на ноль!')
# except ValueError:
#     print('Это калькулятор а не букварь')
# else:
#     print('Всё ок')
# finally:
#     print('Надеюсь ошибок нет')
# lst = []
# f = open('file.txt')
#
# try:
#     f = open('file.txt')
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     try:
#         for line in f:
#             lst.append(int(line))
#     except ValueError:
#         print('убери буквы')
#     else:
#         print('Всё хорошо')
#     finally:
#         f.close()
# print(lst)
# x = input('Введи любое имя: ').lower().strip()
# try:
#     if x == 'артем':
#         raise Exception('не правда')
# finally:
#     print('артем лох')
#
