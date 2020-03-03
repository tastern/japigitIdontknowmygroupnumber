import json
import urllib.request
import requests
	
symbol=input("Get Stock Data 'Quit to Exit'")
while choice != 'quit':
	url="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=choice&apikey=9XBG9KJB3EUIDVYU"
	response = requests.get(url)
	dict = response.json()
	price=(dict.keys()[5])
	print "The current price of choice is: price"
	print "The current price of choice is: price" >> japi.out
	choice=input("Get Stock Data 'Quit to Exit'")