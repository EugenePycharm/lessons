import random as r
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/     
      
                ████──█──█──█──█──████
                █──█──█──█──█─█───█──█
                █──█──████──██────█──█
                █──█─────█──█─█───█──█
                ████─────█──█──█──████      
"""
print(logo)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
player = [r.choice(cards)]
computer = [r.choice(cards)]
score_p = 0
score_c = 0
get_card = "y"
while get_card == 'y':
    player.append(r.choice(cards))

    if sum(player) > 21 and 11 in player:
        for i in range(0, len(player)):
            if player[i] == 11:
                player[i] = 1
                break
    score_p = sum(player)
    print(f"Твоя рука: {player}, Очков: {score_p}")
    print(f"Первая карта диллера: {computer[0]}")
    if score_p > 21:
        get_card = "n"
    else:
        get_card = input(f"Добираем карту? y - да, n - нет\n")
while sum(computer) < 17:
    computer.append(r.choice(cards))
    if sum(computer) > 21 and 11 in computer:
        for i in range(0, len(computer)):
            if computer[i] == 11:
                computer[i] = 1
                break

score_c = sum(computer)
print(f"Рука диллера: {computer}, Очков: {score_c}")
if score_p > 21 and score_c > 21:
    print("Ничья")
elif score_p > score_c:
    print('пабеда')
elif score_p == score_c:
    print("Ничья")
elif score_c > score_p:
    print("Комп фу")
