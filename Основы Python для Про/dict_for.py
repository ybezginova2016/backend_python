friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}


def is_anyone_in(collection, city):
    for friend in collection:
        if collection[friend] == city:
            print('В городе ' + collection[friend] + ' живёт ' + friend + '. Обязательно зайду в гости!')
        else:
            print('В городе ' + collection[friend] + ' у меня есть друг, но мне туда не надо.')


is_anyone_in(friends, 'Хабаровск')