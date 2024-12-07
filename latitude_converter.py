#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from position_converter import PositionConverter


# Convert latitude from DMS, DM and DD to DMS, DM and DD 

# DMS (degrees, minutes, seconds) : 49°30'00"N  (Sexagesimal or base 60)
# DM  (degrees, decimal minutes)  : 49°30,00'S
# DD  (decimal degrees)           : 49,5000°S

class LatitudeConverter(PositionConverter):

    def __init__(self, logger, decimal_separator=','):
        self.logger = logger
        self._decimal_separator = decimal_separator

    def set_card(self, card):
        if card == 'N' or card == 'n':
            self._prefix = ''
        elif card == 'S' or card == 's':
            self._prefix = '-'
        else:
            raise ValueError("Cardinality must be N, n, S or s")
