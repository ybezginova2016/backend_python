def get_together_games(list1, list2):
    # Напишите здесь код функции для поиска пересечений
    set1 = set(list1)
    set2 = set(list2)
    in_both = set1.intersection(set2)
    return in_both

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)
# Напечатайте итоговый перечень игр в цикле
for t in together_games:
    print('👾', t)