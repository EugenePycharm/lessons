import additional
import random
print(additional.logo)

score = 0
data = additional.data
is_game = True
while is_game:
    a = random.choice(data)
    b = random.choice(data)
    print('Твой счет:', score)
    print("-" * 10)
    print(f"А: {a['name']}. {a['description']} из {a['country']}")
    print(additional.vs)
    print(f"B: {b['name']}. {b['description']} из {b['country']}")
    select = input('У кого больше?')
    if select == 'A' or select == 'B':
        if a["follower_count"] > b["follower_count"] and select == "A":
            score = score + 1
        else:
            is_game = False

