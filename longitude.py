#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from coordinate_element import CoordinateElement


# Convert latitude from DMS, DM and DD to DMS, DM and DD 

# DMS (degrees, minutes, seconds) : 49°30'00"W  (Sexagesimal or base 60)
# DM  (degrees, decimal minutes)  : 49°30,00'W
# DD  (decimal degrees)           : 49,5000°W

class Longitude(CoordinateElement):

    def __init__(self, angle, card):
        super().__init__(angle, card)

    def get_prefix(self, card):
        if card == 'E' or card == 'e':
            return ''
        if card == 'W' or card == 'w':
            return '-'
        raise ValueError("Cardinality must be E, e, W or w")
