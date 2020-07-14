
import pandas as pd

read_file = pd.read_excel (r'/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/EBTYH Kylie Music EDL.xlsx')
read_file.to_csv (r'/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv', index = None, header=True)

text = open("/Users/quinn/Desktop/01_Desktop/02 Projects/CueIt/input.csv", "r")
text = ''.join([i for i in text]).replace("_", " ") \
         .replace("copy.01.new.01", "" ) \
         .replace("bounced", "" ) 
x = open("output.csv","w")
x.writelines(text)
x.close()