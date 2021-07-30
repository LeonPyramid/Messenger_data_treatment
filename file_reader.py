import json
import os


def ExtractAllDataFromFolder(directory):
    """Return the dicitonnary stored in each .json file in a list

    Args:
        directory (string): the directory in which the message_x.json are stored

    Returns:
        list(dict): list of all the dictionnary stored in each .json file
    """
    fileNum = 1
    data_list = []
    while(True):
        try:
            file = open(os.path.join(directory,"message_"+str(fileNum)+".json"))
            fileNum += 1
        except FileNotFoundError:
            print(fileNum-1 , " fichiers traités")
            break
        data = json.load(file)
        data_list.append(data)
        
    return data_list
            
            

    