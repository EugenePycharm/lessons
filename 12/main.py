# # lst = [5, 7, "7", True, 5.2, [0, 1, 2, 3, 4, 4, 5], "Вова"]
# # # # # lst.pop(0)  # удалить по индексу
# # # # # lst.remove("7")  # удалить по значению
# # # # # print(lst)
# # # # #
# # # # # lst1 = [0, 1, 2]
# # # # # lst2 = ["A", "B", "C"]
# # # # # lst1.extend(lst2)  # расширить список списком
# # # # # print(lst
# lst = [1, 2, 3]
# # # # # lst.insert(1, 1.5)  # Вставка(индекс, значение)
# # # # # print(lst)
# # # # #
# # # # # lst = [0, 3, 2, 15, -1]
# # # # # lst.sort(reverse=True) # сортировка
# # # # # print(lst)
# # # # #
# # # # # lst.clear() # очистить
# # # # # print(lst)
# # # # # lst = [5, 4, 3, 2, 1]
# # # # # lst.reverse()
# # # # # print(lst)
# # # # # КОРТЕЖИ
# # # # # Типы данных = мутабельные(изменяемые) + немутабельные(неизменяемые)
# # # # #
# # # # # x = "mavavi"
# # # # # x[1] = "o" # так нельзя, питух (str - неизменяемый тип данных)
# # # # #
# # # # # tup = (1, 2, 3)
# # # # # tup1 = 1, 2, 3
# # # # # tup2 = 1,
# # # # # print(max(tup))
# # # # # a = int(input("Число: "))
# # # # # b = int(input("Число: "))
# # # # # lst = []
# # # # # for jojo in range(a + 1, b):
# # # # #     lst.append(jojo ** 2)
# # # # #
# # # # # print(lst)
# # # # phrase = input(" Фраза: ")
# # # # lst = phrase.split(" ") # раскалываем фразу на список
# # # # # lst.reverse()
# # # # # print(lst)
# # # # chet = 0
# # # # nechet = 0
# # # # lst = []
# # # # number = ""
# # # # while number != "end":
# # # #     number = input("Число: ")
# # # #     if number.lstrip("-").isdigit():
# # # #         number = int(number)
# # # #         lst.append(number)
# # # #     elif number == "end":
# # # #         break  # выход из цикла
# # # #     else:
# # # #         print("pon")
# # # #         continue  # перезапуск цикла
# # # #     if number % 2 == 0:
# # # #         chet += 1
# # # #     else:
# # # #         nechet += 1
# # print(f"Чётных: {chet}\n"
# #       f"Нечётных: {nechet}")
# #
# # phrase = input(">>> ")
# # lst = phrase.split(" ")
# # print(lst)
# # for i in range(1, len(lst)):
# #     if int(lst[i]) < int(lst[i-1]):
# #         print(f"Я считаю, что {lst[i]} больше, чем {lst[i-1]}")
# #
# #
# # lst = [-5, 14, 2, -8, 1]
# # mini = min(lst)
# # maxi = max(lst)
# # lst[lst.index(maxi)], lst[lst.index(mini)] = lst[lst.index(mini)], lst[lst.index(maxi)]
# # print(lst)
# # import random
# # lst = []
# # count = int(input("Сколько учеников стоит? (5-20): >>> "))
# # for _ in range(count):
# #     lst.append(random.randint(150, 200))
# # lst.sort(reverse=True)
# # print("Было:", lst)
# #
# # Petya = int(input("Рост Пети: "))
# # lst.append(Petya)
# # lst.sort(reverse=True)
# # print("Стало:", lst)
# #
# # revers = lst[::-1]
# # petya_pos = len(lst) - revers.index(Petya)
# # print(f"Петя встает {petya_pos} по счёту")
#
nums = [4, 5, 6, 7, 8, 9, 10]
shift = int(input("Сдвиг: "))
if shift < 0:
    shift = abs(shift)
    for i in range(shift):
        nums.append(nums.pop(0))
        #  nums.pop - удаляем по индексу первую цифру.
        # nums.append - добавляем в конец
else:
        for i in range(shift):
            nums.insert(0, nums.pop()) #nums.pop() без индекса изымает последний элемент
print(nums)