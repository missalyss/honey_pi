import sys
import Adafruit_DHT
import datetime
import requests
import json
from pytz import timezone
import pytz

while True:
    url = 'https://internet-of-stings.herokuapp.com/humiture'
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    today = datetime.datetime.now()
    pst = timezone('US/Pacific')
    today = pst.localize(today)
    today = today.astimezone(pst)
    date_format = '%m-%d-%y %H:%M:%S %Z'

    today_format = today.strftime(date_format)
    
    query = {'temperature': temperature, 'humidity': humidity, 'date_recorded': today_format, 'user_id': 1}
    
    if today.second % 2 == 0:
        res = requests.post(url, data=query)
        print('Temp: {0:0.1f} C., Humidity: {1:0.1f}%'.format(temperature, humidity), today_format)
