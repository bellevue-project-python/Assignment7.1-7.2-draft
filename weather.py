import json
import requests
api_key = "f249765a9e5e6001ac4ad149953808da"
base_url = "https://api.openweathermap.org/data/2.5/weather"
city_name = input("Enter city name")
complete_url = base_url + "?q=" + city_name + "&appid=" + api_key #complete URL = previoius component parts to create URL
#import urllib.request
def connect (host = 'https://api.openweathermap.org'): #function to test connection
	try:
		requests.get(host)
		return True
	except:
		return False
while True: #proving if connection is available
	if connect():
		print("connected")
		break
	else:
		answer = input("there was a connection error, would you like to try again or exit the program? 1. to exit 2. to try again")
		if answer == '1':
			raise SystemExit
		if answer == '2':
			pass
 # retrieving information from weather API
response = requests.get(complete_url)
x = response.json()
if "cod" !=404:
	y = x["main"]
	current_temp = y["temp"]
	current_pressure = y["pressure"]
	current_humidity = y["humidity"]
	z=x ["weather"]
	weather_description = z [0]["description"]
	print("The Temperature is",str(current_temp)) #Providing retrieved information
	print("The Atmospheric pressure is", str (current_pressure))
	print("The Current humidity level is", str(current_humidity))
	print(str(weather_description))
else:
	print("City Not Found") 