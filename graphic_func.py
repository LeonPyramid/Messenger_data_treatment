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
    """
    Create a one line graph with the frequency of messages

    Parameters
    ----------
    data_list : list(dict)
        Extracter from .json files
    time_res : string
        the resolution of the graph samples. Put "day" or "month"
    directory : string
        the directory where is stored the .json files and where the graph will
        be stored

    Returns
    -------
    None.

    """
    my_dic = {}
    #go through all of the messages files
    for data in data_list:
        #add all existing dates and increase the number off msg by day (or month)
        for msg in data["messages"]:
            date = tmstod(msg["timestamp_ms"]).date();
            if time_res == "month":
                date = (date.year , date.month)
            if date in my_dic:
                my_dic[date] += 1
            else:
                my_dic[date] = 1
    #add a 0 to all non-messaged dates
    end_date = list(my_dic.keys())[0]
    start_date = list(my_dic.keys())[-1]
    if time_res == "day":
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            if not (start_date in my_dic):
                my_dic[start_date] = 0
            start_date += delta
    else:
        while(start_date[0]<end_date[0])or(start_date[1]<end_date[1]):
            if not (start_date in my_dic):
                my_dic[start_date] = 0
            mnth = start_date[1] + 1
            yr = start_date[0]
            if(mnth > 12):
                yr = start_date[0] + 1
                mnth = 1
            start_date = (yr,mnth)
    #sorted revert the list in the right way
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
    #setting plot x axis to date
    plt.plot(x,y)
    #needs to remove some of the label for month, or not readable
    if time_res == "month":
        ax = plt.gca()
        for label in ax.get_xaxis().get_ticklabels()[::2]:
            label.set_visible(False)
    #autofm_date rotate the label
    plt.gcf().autofmt_xdate()
    #save the graph as a png in the subfolder
    plt.savefig(os.path.join(directory,'messages_freq.png'), dpi=300)