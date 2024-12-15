#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pygeodesy import toDMS, parseDMS, F_DMS, F_DM, F_D

# Convert latitude from DMS, DM and DD to DMS, DM and DD 

class Coordinate():

    def __init__(self, degree):
        self.__degree = degree
    
    @classmethod
    def from_str(cls, str_value):
        return cls(parseDMS(f"{str_value}"))

    @classmethod
    def from_dms(cls, degree, minutes, seconds, card):
        # From DMS (degrees, minutes, seconds) : 49°30'00"N  (Sexagesimal or base 60)
        return cls(parseDMS(f"{degree} {minutes} {seconds} {card}"))

    @classmethod
    def from_ddm(cls, degree, minutes, card):
        # From DDM  (degrees, decimal minutes)  : 49°30,00'S
        return cls(parseDMS(f"{degree} {minutes}  {card}"))

    @classmethod
    def from_dd(cls, degree):
        # From DD  (decimal degrees)           : -49,5000°
        return cls(parseDMS(f"{degree}"))

    def to_dms(self):
        return toDMS(self.__degree, F_DMS, prec=0, sep=" ", s_M="'", s_S='"')

    def to_ddm(self):
        return toDMS(self.__degree, F_DM, prec=2, sep=" ", s_M="'")

    def to_dd(self):
        return toDMS(self.__degree, F_D, prec=6)
