#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:41:10 2017

@author: vincent
"""

import csv

def WriteLine(value):
    nl = csv.writer(open("Data_temperature.csv", "wb"))
    nl.writerows(value)
