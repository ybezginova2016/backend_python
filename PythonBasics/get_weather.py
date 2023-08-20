import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'T2': ''
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)