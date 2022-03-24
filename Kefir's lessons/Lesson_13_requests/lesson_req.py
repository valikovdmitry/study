
import requests

# response = requests.get('https://www.google.com/')
# print(response)
#
# con = response.content
# print(con)
#
# requests.get()


# response = requests.get('https://auto.ru/moskva/cars/bmw/5er/22212692/all/engine-dizel/?displacement_from=3000&displacement_to=3000')
# print(response)
#
# con = response.content
# com_decode = response.content.decode()
# print(com_decode)





response = requests.get('https://www.metaweather.com/api/location/search/', params={'query': 'moscow'})
print(response)

city_data = response.json()
print(city_data)

for city in city_data:
    print(city['woeid'])

response = requests.get('https://www.metaweather.com/api/location/search/', params={'query': 'moscow'})
print(response)

