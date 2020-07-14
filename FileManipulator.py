
import pandas as pd 

read_file = pd.read_excel (r'/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/Planet A ep 2 Music EDL.xlsx')
read_file.to_csv (r'/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv', index = None, header=True)

text = open("/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv", "r")
text = ''.join([i for i in text]).replace("_", " ") \
         .replace("copy.01.new.01", "" ) \
         .replace("bounced", "" ) \
         .replace(".wav", "" ) \
         .replace(".", " " ) 
x = open("output.csv","w")
x.writelines(text)
x.close() 

from monkeylearn import MonkeyLearn

ml = MonkeyLearn('fd73e35716bf00e420f5c84e33d8ad44bbff1a4d')
data = ["U/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/CueIt/output.csv"]
model_id = 'ex_d5Cy6Cjr'
result = ml.extractors.extract(model_id, data)
print(result.body)
