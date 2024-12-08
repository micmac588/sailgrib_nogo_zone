#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from coordinate_element import CoordinateElement


# Convert latitude from DMS, DM and DD to DMS, DM and DD 

# DMS (degrees, minutes, seconds) : 49°30'00"N  (Sexagesimal or base 60)
# DM  (degrees, decimal minutes)  : 49°30,00'S
# DD  (decimal degrees)           : 49,5000°S

class Latitude(CoordinateElement):

    def __init__(self, angle, card):
        super().__init__(angle, card)

    def get_prefix(self, card):
        if card == 'N' or card == 'n':
            return ''
        if card == 'S' or card == 's':
            return '-'
        raise ValueError("Cardinality must be N, n, S or s")
