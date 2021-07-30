# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:21:54 2021

@author: Nemes

"""

from timestamp_conv import TimestampmsToDate as tmstod
import datetime
import matplotlib.pyplot as plt
import os

def MessageFreqGraph(data_list,time_res,directory):
    """Create a one line graph with the frequency of messages

    Args:
        data_list (list(dict)):   Extracted from .json files
        time_res (string): the resolution of the graph samples. Put "day" or "month"
        directory (string): the directory where is stored the .json files and where the graph will
        be stored
    """
    
    my_dic = DoubleDictionnaryExtract(data_list,time_res,lambda a : True)[0]
    
    AddEmptyDates(my_dic,time_res)
    
    #must be sorted after adding all the 0 values
    x,y = zip(*sorted(my_dic.items()))
    #convert tuple to string (avoid impossible drawings)
    if time_res == "month":
        tmpx = []
        for elt in x: 
            tmpx.append(str(elt[1])+"\\"+str(elt[0]))
        x = tmpx

    #set a title to the graph
    FolderName = directory.split("\\")[-1]
    fname = FolderName.split("_")
    plt.title(fname[0])

    plt.plot(x,y)
    #needs to remove some of the label for month, or not readable
    if time_res == "month":
        ax = plt.gca()
        for label in ax.get_xaxis().get_ticklabels()[::2]:
            label.set_visible(False)
    #autofm_date rotate the label
    plt.gcf().autofmt_xdate()
    plt.savefig(os.path.join(directory,'messages_freq.png'), dpi=300)

def AddEmptyDates(dict,time_res):
    """creates all entries that doesn't exist yet.
    Put a 0 for value

    Args:
        dict (dict): the (date,value) dictionnary
        time_res (string): the time_resolution
    """
    end_date = list(dict.keys())[0]
    start_date = list(dict.keys())[-1]
    if time_res == "day":
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            if not (start_date in dict):
                dict[start_date] = 0
            start_date += delta
    else:
        while(start_date[0]<end_date[0])or(start_date[1]<end_date[1]):
            if not (start_date in dict):
                dict[start_date] = 0
            mnth = start_date[1] + 1
            yr = start_date[0]
            if(mnth > 12):
                yr = start_date[0] + 1
                mnth = 1
            start_date = (yr,mnth)

def DoubleDictionnaryExtract(data_list,time_res,condition):
    """Creates two dictionnary and add messages in one if condition(message) is true, in the oser else

    Args:
        data_list (list(dict)): the dictionnaries extracted form json
        time_res (string): the resolution of the graph samples. Put "day" or "month"
        condition (func(dict)->bool): a test function used to determine in which dictionnary a message must go

    Returns:
        list(dict): return the list of the two dictionnaries
    """

    dict_0 = {}
    dict_1 = {}
    for data in data_list:
        #add all existing dates and increase the number off msg by day (or month)
        for msg in data["messages"]:
            date = tmstod(msg["timestamp_ms"]).date();
            if time_res == "month":
                date = (date.year , date.month)
            if condition(msg):
                if date in dict_0:
                    dict_0[date] += 1
                else:
                    dict_0[date] = 1
            else:
                if date in dict_1:
                    dict_1[date] += 1
                else:
                    dict_1[date] = 1
    return [dict_0,dict_1]