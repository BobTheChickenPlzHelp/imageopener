import random
from time import sleep
import colorama
import requests
timer = 30
r = requests.get('')
'Requests:' in r.text