# sailgrib_nogo_zone
Build nogo zone kml file for Sailgrib.

Longitude may be incremented automatically (usefull for the Vendee globe ZEA).

You are requested longitude and latitude, type CTRL-C to stop, then a file data.kml is produced.

The last point is automatically added to close the parallelogramme.

You can import it into Sailgrib as a nogo zone.

```bash
python3 sg_nogo_zone.py
first longitude 135
longitude step in degrees 5
longitude (135 00 E)? 
latitude? 50 00 S
longitude (140 00 E)? 
latitude? 50 00 S
longitude (145 00 E)? 
latitude? 50 00 S
longitude (150 00 E)? 50 00 S
Cardinality must be E, e, W or w
longitude (150 00 E)? 
latitude? 50 00 S
longitude (155 00 E)? 
latitude? 56 05 S
longitude (160 00 E)? 
latitude? 56 20 S
longitude (165 00 E)? 
latitude? 56 30 S
longitude (170 00 E)? 
latitude? 56 40 S
longitude (175 00 E)? 
latitude? 56 40 S
longitude (180 00 E)? 
latitude? 56 35 S
longitude (185 00 E)? 180 00 E
latitude? 60 00 S
longitude (185 00 E)? 135 00 E
latitude? 60 00 S
longitude (140 00 E)? ^C
```