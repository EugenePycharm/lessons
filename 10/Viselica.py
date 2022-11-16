import random as r
import pictures
print(pictures.intro)
vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = r.choice(vocabulary).lower()
word_display = []
for _ in range(len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0

while life > 0 and counter != len(word_answer):
    letter = input("Буква: ")
    letter_is_be = False
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != "_":
                letter_is_be = True
            else:
                word_display[i] = letter
                letter_is_be = True
                counter += 1
    if not letter_is_be:
        life -= 1
        print(pictures.stages[life])

if counter == len(word_answer):
    print("ура пабеда")
else:
    print(pictures.stages[life])
    print("проиграл")
