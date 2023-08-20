# вот функция, которая может выбросить исключение
def calc_share(apples, friends):
    # от строки откусываем число и приводим к типу int
    friends_number = int(friends.split()[0])
    return apples/friends_number

# есть 17 яблок
apples = 17

# будем считать, сколько достанется каждому другу
# вызовем функцию calc_share() для разных наших знакомых,
# с различным числом друзей
for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
        try:
                print('Каждому достанется по', calc_share(apples, friends), 'яблока')
        except ZeroDivisionError:
                print('На ноль делить нельзя.')
        except ValueError:
                print(f'Из строки "{friends}" не получилось достать число.')