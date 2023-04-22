#!/usr/bin/python

import random

latitude = random.randrange(37.346389, 37.368889)
longitude = random.randrange(120.414167, 120.4325)
kml = (
   '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
   '<Placemark>\n'
   '<name>Random Placemark</name>\n'
   '<Point>\n'
   '<coordinates>%d,%d</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   '</kml>'
   ) %(longitude, latitude)
print 'Content-Type: application/vnd.google-earth.kml+xml\n'
print kml
