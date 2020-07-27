import pandas as pd 
from csv import reader
from monkeylearn import MonkeyLearn
import json 
import pandas
import jsonlines
#

list = ['CLIP_NAME', 'DURATION']
read_file = pandas.read_excel ('/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/Planet A Ep 3 COVID music EDL.xlsx', usecols=list)
read_file.to_csv ('/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv', index = None, header=True)

text = open("/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv", "r")
text = ''.join([i for i in text]).replace("_", " ") \
         .replace("copy.01.new.01", " " ) \
         .replace("bounced", " " ) \
         .replace(".wav", " " ) \
         .replace(".", " " ) \
         .replace("aiff", " ") \
         .replace("Bounce", " ")\
         .replace("new 01", "")\
         .replace("WAV", "")\
         .replace("wav", "")\
         .replace(".new", "") \
         .replace("AIF", "")
with jsonlines.open('output.jsonl', 'w') as writer:
    writer.write_all(text)







''' colnames = ['CLIP NAME', 'DURATION']
data = pandas.read_csv('output.csv', names=colnames, skiprows=[0])

ml = MonkeyLearn('c85c5f9ffd2391f0a3983d33ac0a0a1226a468e8')
model_id = 'ex_6X6kuExQ'

for e in range(len(data)):
   data = data[e]
   result = ml.extractors.extract(model_id, data)

y = open("processed_batch.csv","w")
y.writelines(finalData)
y.close()
#
data = pandas.read_csv('output.csvcsv', skiprows=[0])
ml = MonkeyLearn('c85c5f9ffd2391f0a3983d33ac0a0a1226a468e8')
model_id = 'ex_6X6kuExQ'
#
for e in data:

   result = ml.extractors.extract(model_id, (str(data[e])))

convertedJson = json.dumps(result.body)
finalOutput = convertedJson
#y = open("processed_batch.csv","w")
#y.writelines(finalOutput)
#y.close()  '''











 





    
    
   



