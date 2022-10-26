# import random as r #использовать рандом как р
# from random import shuffle
# print(r.randint(0, 100))
#
# from random import randint импортировать отдельный модуль
# from random import * имортировать все
# spisok = [1, 2, 3, 4, 5]
# r.shuffle(spisok)
# print(spisok)
# print(r.choice(spisok))
# Черепуха
# import turtle
# t = turtle.Turtle()
# t.begin_fill()
# t.color('purple', 'yellow')
# t.pensize(15)
# horizontal = 200
# vertical = 100
# t.speed(1)
# screen = turtle.Screen()
# t.forward(horizontal)
# t.right(90)
# t.fd(vertical)
# t.right(90)
# t.fd(horizontal)
# t.right(90)
# t.fd(vertical)
# t.end_fill()
# t.penup()
# t.goto(120, -30)
# t.pendown()
# t.goto(180, -30)
# t.circle(radius=20)
# t.write('JENIY', font=('Arial Black', 50, "normal"), align="center")
#
# screen.exitonclick()
# import random as r
# import time
# hacked = 0
# while hacked < 100:
#     hacked = hacked + r.randint(1, 9)
#     time.sleep(1)
#     if hacked >= 100:
#         print("Прогресс:100%")
#     else:
#         print(f"Прогресс:{hacked}%")
#
# var = ["1️⃣, 2️⃣, 3️⃣"]
# print(var[0])
# import turtle
# import random
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(1)
# t.pencolor("pink")
# t.pensize(10)
# colors = ["yellow", "pink", "purple", "orange", "red", "blue"]
# i = int(input('Количество углов: '))
# side = 100
#
# for j in range(0, i):
#     t.color(random.choice(colors))
#     t.fd(side)
#     t.rt(360/i)
# screen.exitonclick()
import time
import random

patron = random.choice([1, 2, 3, 4, 5, 6])
zar = random.choice([1, 2, 3, 4, 5, 6])

print("Заряжаем питон..")
time.sleep(1)
print("Крутиим барабашку..")
time.sleep(2)
print("Выстрел через:")
time.sleep(1)
print('3')
time.sleep(1)
print("2")
time.sleep(1)
print('1')
time.sleep(1)
if patron == zar:
    print('Повезет в другой раз))')
else:
    print('Повезло')
