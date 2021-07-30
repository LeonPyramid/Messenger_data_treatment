# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:23:05 2021

@author: Romain Delpy & Emile Egreteau-Druet
"""



import os
import graphic_func
import file_reader

direc =  os.path.join(os.getcwd(), "messages")
for folderName in os.listdir(direc):
    curdir = os.path.join(direc, folderName)
    if os.path.isdir(curdir):
        data_list = file_reader.ExtractAllDataFromFolder(curdir)
        graphic_func.MessageFreqGraph(data_list,"month", curdir)
        graphic_func.UserIndividualGraph(data_list,"month",curdir)
