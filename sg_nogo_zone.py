
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from coordinate import Coordinate
import logging
import signal
import sys
from jinja2 import Environment, FileSystemLoader

def handler(signum, frame):
    global parallelogramme
    parallelogramme = close_parallelogramme(parallelogramme)
    template = Environment(loader=FileSystemLoader('templates')).get_template('nogo_zone.kml')
    rendered = template.render(nogo_zone=parallelogramme)
    with open("data.kml", "w") as f:
	    f.write(rendered)
    sys.exit(0)

def position(lat, lon):
    return  f"{lon},{lat},0 "

def close_parallelogramme(para):
    first = para.split(' ')[0]
    return para + first

signal.signal(signal.SIGINT, handler)

parallelogramme = ""
my_logger = logging.getLogger()
# TODO my_logger.setLevel(logging.DEBUG)
longitude = int(input("first longitude "))
step = int(input("longitude step in degrees "))
while (True):
    try:
        degrees, minutes, card = input(f"longitude ({longitude} 00 E)? ").split() or f"{longitude} 00 E".split()
        longitude = Coordinate.from_ddm(int(degrees),float(minutes),str(card)).to_dd().split('°')[0]
        my_logger.error(f"longitude {longitude}")
        degrees, minutes, card = input(f"latitude? ").split()
        latitude = Coordinate.from_ddm(int(degrees),float(minutes),str(card)).to_dd().split('°')[0]
        my_logger.error(f"latitude {latitude}")
        parallelogramme = parallelogramme + position(latitude, longitude)
        longitude = int(longitude.split('.')[0]) + step
    except Exception as e:
        my_logger.error(e)
