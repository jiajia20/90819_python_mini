import requests
from bs4 import BeautifulSoup

# Create the http request and request the page
# prompt the user for a latitude
latitude = input('key in latitude: \n')
longitude =  input('key in longitude: \n')

#Then construct the URL by concatenating forecast.weather.gov with your latitude and longitude:
httpString ='https://forecast.weather.gov/MapClick.php?textField1=' + latitude + '&textField2=' + longitude
#httpString ='https://forecast.weather.gov/MapClick.php?textField1=40.47&textField2=-79.96'
print(httpString)
page = requests.get(httpString)

# Scraping:


# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')
# Find the required tag
seven_day = soup.find(id="seven-day-forecast")
# Find the sub-tag
forecast_items = seven_day.find_all(class_="tombstone-container")
# Get the thing
tonight = forecast_items[0]
print(tonight.prettify())

# Find the other data
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)


# Find the required tag
details = soup.find(id="current_conditions_detail")
detail_items = details.find_all('td')
result = []
for item in detail_items:
    result.append(item.get_text())

# identifty the items 
humidity = result[1]
Wind_Speed = result[3]
Barometer = result[5]
Dewpoint = result[7]
Visibility = result[9]
Wind_Chill = result[11]
Last_update = result[13]

# print the results
print('humidity: ', humidity)
print('Wind_Speed: ', Wind_Speed)
print('Barometer: ', Barometer)
print('Dewpoint: ', Dewpoint)
print('Visibility: ', Visibility)
print('Wind_Chill: ', Wind_Chill)
print('Last_update: ', Last_update.strip())