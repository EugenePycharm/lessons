alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
should_end = False

while not should_end:
    text = input("Введи сообщение: ")
    text = list(text)
    shift = int(input("Сдвиг: "))

    # механизм сдвига
shifr = ""
for letter in text:
    if letter == "":
        shifr += letter
else:
    position = alphabet.index(letter)
    if position + shift > len(alphabet):
        new_position = position + shift - len(alphabet)
    elif position + shift < 0:
        new_position = position + shift + len(alphabet)
    else:
        new_position = position + shift
    shifr = alphabet[new_position]
