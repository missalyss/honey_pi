import sys
import Adafruit_DHT

def humiture():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    if humidity is not None and temperature is not None:
            print('Temp: {0:0.1f} C. Humidity: {1:0.1f}%'.format(temperature, humidity))
    else:
            print('failed to get reading')
            sys.exit(1) 
humiture()