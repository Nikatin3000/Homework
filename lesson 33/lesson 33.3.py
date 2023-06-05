import requests

API_KEY = '072e332c321805809b1e54b0d6c4a542'

def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        result = f'Погода в місті {city_name}:\n'
        result += f'Температура: {temperature}°C\n'
        result += f'Вологість: {humidity}%\n'
        result += f'Опис: {description}\n'

        return result
    else:
        return None

city = input('Введіть назву міста: ')

weather = get_weather(city)

if weather:
    print(weather)
else:
    print('Не вдалося отримати погоду. Спробуйте ще раз або перевірте підключення до Інтернету.')


# це приклад посилання але чомусь сайт свариця на АРІ ключ хоча він правильний

# Endpoint:
# - Please, use the endpoint api.openweathermap.org for your API calls
# - Example of API call:
# api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=072e332c321805809b1e54b0d6c4a542
