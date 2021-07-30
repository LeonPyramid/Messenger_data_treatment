# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:05:27 2021

@author: Nemes
"""

from datetime import datetime as dtm


def TimestampmsToDate(timestamp):
    timestamp = timestamp // 1000;
    date = dtm.fromtimestamp(timestamp)
    return date;