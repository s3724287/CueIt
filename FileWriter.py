#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas
import pandas as pd
import numpy as np
from string import digits
import re
from csv import reader
import csv
#
#text = open("/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/CueIt/processed_batch.csv", "r")
#text = ''.join([i for i in text]).replace(" ", "") 
#x = open("analysed.csv","w")
#x.writelines(text)
#x.close() 
#
libcolnames = ['PREFIX', 'LABEL']
data = pandas.read_csv('MusicLibraries.csv', names=libcolnames, skiprows=[0])
#
fincolnames = ['composer', 'trackID', 'trackNumber', 'duration', 'publisher']
finalData = pandas.read_csv('processed_batch.csv', names=fincolnames, skiprows=[0])
#
for e in range(len(finalData)):
    me = finalData['trackID'][e]
    for i in range (len(data['PREFIX'])):
        if re.match(str(data['PREFIX'][i]), str(me)):
            
         finalData['publisher'][e] = (str(data['LABEL'][i]))
#
finalData.to_csv('final.csv')        
