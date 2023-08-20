import datetime as dt # module

# dt.datetime - вызов класса
# https://docs.python.org/3/library/datetime.html

start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

# Дата и время посадки: 1961 год, 12 апреля, 10 часов, 55 минут
landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)

print(landing_time - start_time)


# Дата выхода первой серии.
start_time = dt.datetime(2011, 4, 17)
# Укажите дату выхода последней серии.
final_time = dt.datetime(2019, 4, 15)

# Вычислите, сколько времени шёл сериал.
duration = final_time - start_time
print(duration)


start_moment = dt.datetime(2022, 6, 11, 22, 30, 0) # Напишите код здесь
current_moment = dt.datetime(2023, 8, 14, 23, 30, 0)  # и здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)

# utcnow() is a method within a class of the module
print(dt.datetime.utcnow())

"""
utc_time = dt.datetime.utcnow(): Here, you're accessing the datetime class within 
the datetime module using the alias dt, and then you're calling the utcnow() 
method of that class to get the current UTC time as a datetime object.

"""

import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(city):
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city
    hours = dt.datetime.utcnow()
    time_delta = dt.timedelta(hours = UTC_OFFSET[city])
    final_time = hours + time_delta
    return final_time

print(what_time('Екатеринбург'))

##########################################

"""
The correct way to create a datetime object representing 
the current time is to directly use the class constructor without parentheses
"""

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    time_now = dt.datetime.utcnow()
    city = DATABASE[friend]
    time_delta = dt.timedelta(hours=UTC_OFFSET[city])
    final_time = time_now + time_delta
    return final_time


print(what_time('Соня'))