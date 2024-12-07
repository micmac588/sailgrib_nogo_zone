#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import sys
import re
import logging

my_logger = logging.getLogger()

# https://www.fcc.gov/media/radio/dms-decimal

##
# Convert degrees from DMS, DM and DD to DMS, DM and DD 
#
# Input value may be a string
#   DMS (degrees, minutes, seconds) : 49°30'00"  (Sexagesimal or base 60)
#   DDM (degrees, decimal minutes)  : 49°30,00'
#   DD  (decimal degrees)           : 49,5000°
#   Spaces are also supported between degrees and minutes and between minutes and seconds


class DegreeConverter:

    DMS_PATTERN = r"(?P<degrees>\d{1,3})°\s?(?P<minutes>\d{1,2})'\s?(?P<seconds>\d{2})\""
    DDM_PATTERN  = r"(?P<degrees>\d{1,3})°\s?(?P<minutes>\d{1,2})[,.](?P<cminutes>\d{2})'"
    DD_PATTERN  = r"(?P<degrees>\d{1,3})[,.](?P<dmdegree>\d{4})°"


    def __init__(self, logger, decimal_separator=','):
        self._logger = logger
        self._decimal_separator = decimal_separator

    def from_str(self, value):
        match_dms = re.match(self.DMS_PATTERN, value)
        match_ddm = re.match(self.DDM_PATTERN, value)
        match_dd = re.match(self.DD_PATTERN, value)
        if match_dms:
            self.degrees = int(match_dms['degrees'])
            self.minutes = int(match_dms['minutes'])
            self.seconds = int(match_dms['seconds'])
            self._logger.debug(f'input dms : {self.degrees}/{self.minutes}/{self.seconds}')
        elif match_ddm:
            self.degrees = int(match_ddm['degrees'])
            self.minutes = int(match_ddm['minutes'])
            self.seconds = int(int(match_ddm['cminutes']) * 60/100)
            self._logger.debug(f'inoput ddm : {self.degrees}/{self.minutes}/{self.seconds}')
        elif match_dd:
            self.degrees = int(match_dd['degrees'])
            self.minutes = int(int(match_dd['dmdegree']) * 60/10000)
            self.seconds = round(((int(match_dd['dmdegree']) * 60/10000) % 1) * 60)
            self._logger.debug(f'input dd : {self.degrees}/{self.minutes}/{self.seconds}')
        else:
            raise ValueError(f"format of {value} not supported")
        return self
        
    def from_dms(self,degree, minutes, seconds):
        self.degrees = degree
        self.minutes = minutes
        self.seconds = seconds
        self._logger.debug(f'input dms : {self.degrees}/{self.minutes}/{self.seconds}')
        return self

    def from_ddm(self,degree, minutes):
        self.degrees = degree
        self.minutes = int(minutes)
        self.seconds = 60 * (minutes%1) 
        self._logger.debug(f'input ddm : {self.degrees}/{self.minutes}/{self.seconds}')
        return self

    def from_dd(self,degree):
        self.degrees = int(degree)
        self.minutes = 60 * (degree%1)
        self.seconds = 60 * ((60 * (degree%1))%1)
        self._logger.debug(f'input ddm : {self.degrees}/{self.minutes}/{self.seconds}')
        return self

    def to_dms(self):
        return f"{self.degrees}° {self.minutes}' " + (f"{int(self.seconds)}").zfill(2) + '"'

    def to_ddm(self):
        return f"{self.degrees}° {self.minutes + self.seconds/60:.2f}".replace('.', self._decimal_separator) + "'"

    def to_dd(self):
        return f"{(self.degrees + self.minutes/60 + self.seconds/3600):.6f}".replace('.', self._decimal_separator) + "°"
    
if __name__ == "__main__":
    dd = DegreeConverter(my_logger).from_str(sys.argv[1]).to_ddm()
    print(dd)
