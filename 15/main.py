#  Множества надмножества и подмножества
# s = {1, 2, 3}
# nad = {0, 1, 2, 3}
# pod = {1, 2}
# mis = {4, 5}
# if pod < s:
#     print("Это подмножество S")
# person_1 = {"Python", "C#", "Java"}
# person_2 = {"YoptaScript", "Kotlin", "BrainFuck", "C++", "Python"}
# if person_1 < person_2:
#     print("второй круче он знает стэк первого")
# elif person_2 < person_1:
#     print("первый крутой")
# else:
#     print("Стэки отличаются")
# def Donbas():
#     print("5")
#     print("4")
#     print("3")
#     print("2")
#     print("1")
# Donbas()
# Donbas()
# def koren(number, stepen):  # функция с двумя аргументами
#     return number == (1 / stepen)  # возвращение результата
#
#
# print(koren(27, 3))
# Первый задача
# def is_sorted(spisok):
#     s = sorted(listik)
#     if s == spisok:
#         return True
#
#
# listik = [1, 2, 3]
# is_sorted(spisok=listik)
# if is_sorted(listik):
#     print("kruto")
# else:
#     print("nekruto")
# Вторая задача
#
# def find_longest(words):
#     chisla = []
#     for churka in words:
#         chisla.append(len(churka))  # добавляем длину каждого слова
#
#     maxi = max(chisla)  # максимальная длина из списка
#     index = chisla.index(maxi)  # индекс наибольшей длины
#     return words[index]
#
#
# spisok = ["donbas", "afganistan", "iraq", "papich"]
# print(find_longest(words=spisok))
# Задача 3
# def min_max(spisok):
#     mini, maxi = spisok[0], spisok[0]
#     for i in spisok:
#         if i > maxi:  # нахождение нового максимума
#             maxi = i  # запись нового максимума
#         if i < mini:
#             mini = i
#     return {"максимум": maxi, "минимум": mini}
#
#
# listik = [1, 2, 3, 4]
# print(min_max(spisok=listik))
# Задача 4
# def list_sum(l1, l2):
#     if len(l1) != len(l2):
#         if len(l1) > len(l2):
#             for index in range(len(l2)):
#                 l1[index] += l2[index]
#                 return l1
#         else:
#             if len(l2) != len(l1):
#                 if len(l2) > len(l1):
#                     for index in range(len(l2)):
#                         l2[index] += l1[index]
#                     return l2
#
#
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [5, 6, 7]
#
# print(list_sum(lst1, lst2))
# Задача 5
def tajik(number):
    for i in range(2, number + 1):
        if i == number:
            return True

        if number % i == 0:
            break


print(tajik(4))
