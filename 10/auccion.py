import os
bets = []
trigger = "yes"
while trigger == "yes":
    name = input("Имя: ")
    bet = int(input("Ставка: "))
    temp_bet = {"name": name, "bet": bet}
    bets.append(temp_bet)

    trigger = input("Продолжаем? Yes || No")
    os.system("cls||clear")
winner = {'name': "", "bet": 0}
for i in range(len(bets)):
    if bets[i]['bet'] > winner['bet']:
        winner['name'] = bets[i]['name']
        winner['bet'] = bets[i]['bet']
print(f"Победитель: {winner['name']} и его ставка: {winner['bet']}")
