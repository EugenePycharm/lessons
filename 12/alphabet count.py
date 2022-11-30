alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
sentence = 'Ha ocнoвe вceгo вышecкaзaннoгo, xoчy oтмeтить, чтo oсoбo пpиcтaльнoe внимaниe cтoит yдeлить нa ' \
           'aкцию "oдин плюc oдин" '
sentence = sentence.lower()
missing = ''
for letter in alphabet:
    if letter not in sentence:
        missing = missing + letter
if len(missing) != 0:
    print("missing", missing)
else:
    print("pon")
