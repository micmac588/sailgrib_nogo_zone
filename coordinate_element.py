#!/usr/bin/python3
# -*- coding: utf-8 -*-
import abc
from angle import Angle

# Convert latitude from DMS, DM and DD to DMS, DM and DD 

class CoordinateElement():

    def __init__(self, angle, card):
        self.__angle = angle
        self.__card = card
 
    @abc.abstractmethod
    def get_prefix(self, card):
        return
    
    @classmethod
    def from_str(cls, str_value, card):
        return cls(Angle.from_str(str_value), card)

    @classmethod
    def from_dms(cls, degree, minutes, seconds, card):
        # DMS (degrees, minutes, seconds) : 49°30'00"N  (Sexagesimal or base 60)
        return cls(Angle.from_dms(degree, minutes, seconds), card)

    @classmethod
    def from_ddm(cls, degree, minutes, card):
        # DDM  (degrees, decimal minutes)  : 49°30,00'S
        return cls(Angle.from_ddm(degree, minutes), card)

    @classmethod
    def from_dd(cls, degree, card):
        # DD  (decimal degrees)           : 49,5000°S
        return cls(Angle.from_dd(degree), card)

    def to_dms(self):
        return f"{self.get_prefix(self.__card)}{self.__angle.to_dms()}"

    def to_ddm(self, decimal_separator='.'):
        return f"{self.get_prefix(self.__card)}{self.__angle.to_ddm(decimal_separator)}"

    def to_dd(self, decimal_separator='.'):
        return f"{self.get_prefix(self.__card)}{self.__angle.to_dd(decimal_separator)}"
