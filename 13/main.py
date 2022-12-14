# set()  # преобразование во множество
# myset = {"a", "l", "d", "f"}
# myset = {"a", "l", "d", [True]}
# print(myset)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1 | set2)  # обьединение множеств
# print(set1 & set2)  # пересеченме
# print(set1 - set2)  # разность
# print(set1 ^ set2)  # симметрическая разность
#
# # Словарь
# mylist = {"ключик1": 1,
#           "ключик2": "2"
#           }
# from random import randint
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst)
# print(f"Уникальных: {len(unique)} {unique}")
# from random import randint
# size = randint(100, 1000)
# r_start = 0
# r_end = 10000
# lst1 = []
# lst2 = []
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
#
# set1 = set(lst1)
# set2 = set(lst2)
# overall = set1.intersection(set2)
# print(f"Всего {len(overall)}")
# print(f"Кол-во генераций: {size}")
# print(f"Минимальное: {min(overall)}")
# print(f"Максимальное: {max(overall)}")
# print(sorted(overall))
# set1 = set()  # создание пустого множества
# insert = ""
# while insert != "end":
#     insert = input("Число: ")
#     if insert.lstrip("-").isdigit():
#         if insert not in set1:
#             print("НЕТ")
#             set1.add(insert)
#         else:
#             print("ДА")
#     elif insert == "end":
#         break
#     else:
#         print("number!!!")
# lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# print(f"{lst1} - возможно есть повторения")
# set1 = set(lst1)
# print(f"{set1} - точно повторений нет")
# if len(lst1) != len(set1):
#     print("Повторения есть")
# else:
#     print("Повторений нет")
# print(f"Повторений: {len(lst1) - len(set1)}")
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/',
#            ':', ';']
# phrase = "Я люблю movavi, программирование, а ещё я люблю пельмени!"
# text = ""
# for char in phrase:
#     if char not in symbols:
#         text = text + char
# text = text.split(" ")
# print(text)
# s = set(text)
# print(s)
# print(f"Различных слов {len(s)}")
gen = {}
n = int(input("Кол-во связей: "))
for _ in range(n):
    child, parent = input("Ребенок, Родитель").upper().split()
    if parent not in gen:  # если еще нет в древе
        gen[parent] = [child]
    else:
        gen[parent].append(child)  # добавляем ребенка
print(gen)