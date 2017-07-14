import sys
import Adafruit_DHT
import datetime
import requests
import json

while True:
    url = 'https://internet-of-stings.herokuapp.com/humiture'
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    today = datetime.datetime.now()
    query = {'temperature': temperature, 'humidity': humidity, 'date_recorded': today, 'user_id': 1}
    
    if today.second % 2 == 0:
        #res = requests.post(url, data=query)
        print(today.strftime('%m-%d-%y %H:%M:%S %z-0800'))
        #print("{today}", "{today.month} {today.day} {today.hour}:{today.minute}:{today.second}")
        #print(query)
        #print('Temp: {0:0.1f} C., Humidity: {1:0.1f}%'.format(temperature, humidity))
