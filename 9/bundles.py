import random as r
answer = r.randint(100, 999)
length = 3
life = 10
answer = str(answer)
answer = list(answer)
print("Правильный ответ", answer)
while life:
    is_guessed = False
    print("=" * 10)
    print(f"Жизнй:{life}")

    guess = input("Предположение: ")
    if len(guess) != 3 or not guess.isdigit():
        print("Число от 100 до 999 пж")
        continue
    if list(guess) == answer:
        print('харошо')
        is_guessed = True
        break
    if not is_guessed:
        for i in range(0, length):
            if guess[i] == answer[i]:
                print('2✔')
                life -= 1
                is_guessed = True
                break
    if not is_guessed:
        for char in guess:
            if char in answer:
                print('1✔')
                life -= 1
                is_guessed = True
                break
        if not is_guessed:
            print("piko :(")
            life -= 1

