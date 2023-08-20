import requests

# документация про другие параметры: https://wttr.in/:help?lang=ru

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'T': '',
    'M': '', # без значения — чтобы скорость ветра была в метрах в секунду, как принято у метеорологов
    'lang': 'ru' # со значением ru, чтобы прогноз выдавался на русском языке
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)