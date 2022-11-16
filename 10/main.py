# while True:
#     try:
#         x = int(input("Ярусов: "))
#         if x < 1:
#             raise Exception("Положительное нада")
#     except ValueError:
#         print("Ошибочка")
#         continue
#     except Exception:
#         print('неа')
#     else:
#         break
# while True:
#     symbol = input("Символ: ").strip()
#     if len(symbol) != 1:
#         print("Один символ!")
#         quit()
#     for numbers in range(1, x+1):
#         print(" " * (x - numbers), end="")
#         print(symbol * numbers, end="|")
#         print(symbol * numbers)
#
#
# x = int(input('чесло: '))
# for number in range(1, 11):
#     print(x, "x", number, "=", x * number)

ids = int(input("Ширина: "))
idv = int(input("Высота: "))
znak = input("Znak: ")
for _ in range(idv):
    print(znak * ids)

