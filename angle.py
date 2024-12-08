#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

class Angle():

    DMS_PATTERN = r"(?P<degrees>\d{1,3})°\s?(?P<minutes>\d{1,2})'\s?(?P<seconds>\d{2})\""
    DDM_PATTERN  = r"(?P<degrees>\d{1,3})°\s?(?P<minutes>\d{1,2})[,.](?P<cminutes>\d{2})'"
    DD_PATTERN  = r"(?P<degrees>\d{1,3})[,.](?P<dmdegree>\d{4})°"

    def __init__(self, degrees, minutes, seconds):
        self.__degrees = degrees
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__degrees} {self.__minutes} {self.__seconds}"
    
    @classmethod
    def from_str(cls, str_value):
        match_dms = re.match(cls.DMS_PATTERN, str_value)
        match_ddm = re.match(cls.DDM_PATTERN, str_value)
        match_dd = re.match(cls.DD_PATTERN, str_value)
        if match_dms:
            return cls(int(match_dms['degrees']), 
                       int(match_dms['minutes']), 
                       int(match_dms['seconds']))
        if match_ddm:
            return cls(int(match_ddm['degrees']),
                       int(match_ddm['minutes']),
                       int(int(match_ddm['cminutes']) * 60/100))
        if match_dd:
            return cls(int(match_dd['degrees']),
                       int(int(match_dd['dmdegree']) * 60/10000),
                       round(((int(match_dd['dmdegree']) * 60/10000) % 1) * 60))
        
        raise ValueError(f"format of {str_value} not supported")

    
    @classmethod
    def from_dms(cls,degree, minutes, seconds):
        return cls(degree, minutes, seconds)

    @classmethod
    def from_ddm(cls,degree, minutes):
        return cls(degree, int(minutes), 60 * (minutes%1))

    @classmethod
    def from_dd(cls,degree):
        return cls(int(degree), int(60 * (degree%1)), 60 * ((60 * (degree%1))%1))

    def to_dms(self):
        return f"{self.__degrees}° {self.__minutes}' " + (f"{round(self.__seconds)}").zfill(2) + '"'

    def to_ddm(self, decimal_separator='.'):
        return f"{self.__degrees}° {self.__minutes + self.__seconds/60:.2f}".replace('.', decimal_separator) + "'"

    def to_dd(self, decimal_separator='.'):
        return f"{(self.__degrees + self.__minutes/60 + self.__seconds/3600):.6f}".replace('.', decimal_separator) + "°"