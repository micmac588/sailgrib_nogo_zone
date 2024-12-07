#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from position_converter import PositionConverter


# Convert latitude from DMS, DM and DD to DMS, DM and DD 

# DMS (degrees, minutes, seconds) : 49°30'00"W  (Sexagesimal or base 60)
# DM  (degrees, decimal minutes)  : 49°30,00'W
# DD  (decimal degrees)           : 49,5000°W

class LongitudeConverter(PositionConverter):

    def __init__(self, logger, decimal_separator=','):
        self.logger = logger
        self._decimal_separator = decimal_separator

    def set_card(self, card):
        if card == 'E' or card == 'e':
            self._prefix = ''
        elif card == 'W' or card == 'w':
            self._prefix = '-'
        else:
            raise ValueError("Cardinality must be E, e, W or w")
