#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas
import pandas as pd
import numpy as np
from string import digits
import re
from csv import reader
import csv
from datetime import datetime
#
#text = open("/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/CueIt/processed_batch.csv", "r")
#text = ''.join([i for i in text]).replace(" ", "") 
#x = open("analysed.csv","w")
#x.writelines(text)
#x.close() 
#                                                                    
libcolnames = ['PREFIX', 'LABEL', 'PUBLISHER']
data = pandas.read_csv('MusicLibraries.csv', names=libcolnames, skiprows=[0])
#
fincolnames = ['trackTitle', 'duration', 'trackNumber', 'trackID']
finalData = pandas.read_csv('EP1processed_batch (1).csv', names=fincolnames, skiprows=[0], usecols=['trackTitle', 'duration', 'trackNumber', 'trackID',])
#
finalData1 = pandas.DataFrame(columns=['composer', 'record-label', 'publisher', 'hr', 'min', 'sec', 'frames'], index=finalData.index )
#
finalData["duration"].fillna("00:00:00:00", inplace = True)
#
for d in range(len(finalData)):
    
   #a = str(finalData['duration'][d]).split(":")

  finalData1['hr'][d], finalData1['min'][d], finalData1['sec'][d], finalData1['frames'][d] = str(finalData['duration'][d]).split(":")
  
   #print(a)

   

#finalData1['hr'][d]  = str(a[0])
#finalData1['min'][d] = str(a[1])
#finalData1['sec'][d] = str(a[2])
#
for e in range(len(finalData)):
    me = finalData['trackID'][e]
    for i in range (len(data['PREFIX'])):
        if re.match(str(data['PREFIX'][i]), str(me)):
            
         finalData1['record-label'][e] = (str(data['LABEL'][i]))
         finalData1['publisher'][e] = (str(data['PUBLISHER'][i]))
#
dataExport = finalData.append(finalData1)
dataExport.to_csv('EP1final.csv')        
