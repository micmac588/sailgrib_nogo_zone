#!/usr/bin/python3
# -*- coding: utf-8 -*-
import abc
from degree_converter import DegreeConverter


# Convert latitude from DMS, DM and DD to DMS, DM and DD 

# DMS (degrees, minutes, seconds) : 49°30'00"N  (Sexagesimal or base 60)
# DM  (degrees, decimal minutes)  : 49°30,00'S
# DD  (decimal degrees)           : 49,5000°S

class PositionConverter():

    def __init__(self, logger, decimal_separator=','):
        self.logger = logger
        self._decimal_separator = decimal_separator
        self._prefix = ''

    @abc.abstractmethod
    def set_card(self, card):
        return

    def from_dms(self,degree, minutes, seconds, card):
        self.__dc = DegreeConverter(self.logger, self._decimal_separator).from_dms(degree, minutes, seconds)
        self.set_card(card)
        return self

    def from_ddm(self,degree, minutes, card):
        self.__dc = DegreeConverter(self.logger, self._decimal_separator).from_ddm(degree, minutes)
        self.set_card(card)
        return self

    def from_dd(self,degree, card):
        self.__dc = DegreeConverter(self.logger, self._decimal_separator).from_dd(degree)
        self.set_card(card)
        return self

    def to_dms(self):
        return f"{self._prefix}{self.__dc.to_dms()}"

    def to_ddm(self):
        return f"{self._prefix}{self.__dc.to_ddm()}"

    def to_dd(self):
        return f"{self._prefix}{self.__dc.to_dd()}"
