import sys
import datetime
#import requests
#import json
import pytz
from pytz import timezone


#while True:

today = datetime.datetime.now()
pst = pytz.timezone('US/Pacific')
uct = timezone('US/Eastern')
today = pst.localize(today)
today = today.astimezone(pst)
#today_pst = today.replace(tzinfo=timezone('US/Pacific'))
date_format = '%m-%d-%y %H:%M:%S'
print(today.strftime(date_format))

#'curr ', current.strftime(date_format)
