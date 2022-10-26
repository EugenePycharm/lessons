import random

while True:
    print("Угадай число")
    d = input('Введи максимальное число для угадывания:')
    if d.isdigit():
        d = int(d)
    if d < 1:
        raise Exception
    mini = 0
    maxi = d
    computer_number = random.randint(0, d)
    life = 7
    while life > 0:
        try:
            user_number: int = int(input("Введи число: "))
        except ValueError:
            print('Нужна цифра')
            continue
        if user_number < 0 or user_number > d:
            print(f"Введи число от 0 до {d}")
            continue
        if computer_number == user_number:
            print("Вы победили!")
            break
        elif computer_number < user_number:
            print("Нужно меньше.")
            maxi = user_number
        else:
            print("Нужно больше.")
            mini = user_number
        print(f">>> Интервал: {mini} – {maxi}")
        life = life - 1
        print("❤️:", life)
    answer = input("Хочешь продолжить?")
    if answer == "Да":
        continue
    else:
        break
