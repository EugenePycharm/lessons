# name = input('Имя:').capitalize()
# familia =  input('Фамилия:').capitalize()
# otchestvo = input('Отчество:').capitalize()
# print(familia, name[0] + '.',otchestvo[0] + '.')
# print(f'{familia} {name[0]}.{otchestvo[0]}.')
# №2
# x = 'bambazaver'
# print(x.count('a'))
# x = 'hello world'
# lst =  x.split(" ") #словарь
# lst.pop(0) #удаление по индексу
# print(lst)
# x = input('введи фразу')
# trans = ""
# alfa = {
# 'и': 'i',
# 'а': 'a',
# 'ё': 'yo',
# 'о': 'o',
# 'р': 'r',
# 'х': 'h',
# 'ж': 'j',
# 'л': 'l',
# 'п': 'p',
# 'т': 't',
# 'д': 'd',
# 'с': 's',
# 'ц': 'c',
# 'в': 'v',
# 'н': 'n',
# 'е': 'e',
# 'м': 'm',
# ' ': ' ',
# }
# for bukwa in x:
#     trans = trans + alfa[bukwa]
# print(trans)
# x = 5
# if x == 5:
#     print('урааааааааааааааааааааааааааааааааааааааааааааа')
# x = int(input('vvedi chislo'))
# if x < 0:
#     print('отрицатеьное')
# elif x > 0:
#     print('положительное')
# else:
#     print('равно')
year = int(input('Год: '))
if year % 4 == 0 or year % 400 == 0 and year % 100 == 0:
    print('Весокосный')
else:
    print('Не весокосный')
