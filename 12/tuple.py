from collections import namedtuple

citizen = namedtuple("Гражданин", "Имя Возраст Статус")
leha = citizen(Имя="Лёха Лепеха",
               Возраст=27,
               Статус="Бездарь")
print(leha.Имя)
print(leha.Возраст)
print(leha.Статус)