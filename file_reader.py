# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:23:05 2021

@author: Nemes
"""

#global var

import json
import os
import graphic_func

def ExtractAllDataFromFolder(directory):
    """
    Return the dicitonnary stored in each .json file in a list

    Parameters
    ----------
    directory : string
        the directory in which the message_x.json are stored

    Returns
    -------
    data_list : list(dict)
        list of all the dictionnary stored in each .json file

    """
    fileNum = 1
    data_list = []
    while(True):
        try:
            file = open(os.path.join(curdir,"message_"+str(fileNum)+".json"))
            fileNum += 1
        except FileNotFoundError:
            print(fileNum-1 , " fichiers traités")
            break
        data = json.load(file)
        data_list.append(data)
        
    return data_list


######      MAIN         ######
#open the fodler message, where all the subfolders are

direc =  os.path.join(os.getcwd(), "messages")
for folderName in os.listdir(direc):
    curdir = os.path.join(direc, folderName)
    if os.path.isdir(curdir):
        data_list = ExtractAllDataFromFolder(curdir)
        graphic_func.MessageFreqGraph(data_list,"month", curdir)

            
            

    