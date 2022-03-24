import requests
import json


response_cities_data = requests.get('https://www.metaweather.com/api/location/search/', params={'query': 'san '})
cities_data = response_cities_data.json()
print(cities_data)
'''   Забрали данные для 'moscow' в Location Search.   '''
'''   Обернули контент в json и проинициализировали его.   '''


# with open('data/cities_data.json', 'w') as f:
#     json.dump(cities_data, f,  indent=4)
# '''   Теперь у нас есть вся инфа по городу в json. Нам нужно забрать только 'woeid'.   '''

name_woeid = dict()
for city in cities_data:
    name_woeid[city["title"]] = city['woeid']
print(name_woeid)


for name, woeid in name_woeid.items():
    weather_response = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
    weather_data = weather_response.json()

    with open(f'data/{name}.json', 'w') as f:
        json.dump(weather_data, f, indent=4)




