
import pandas as pd

read_file = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)





text = open("input.csv", "r")
text = ''.join([i for i in text]).replace("_", " ") \
         .replace("copy.01.new.01", "" ) \
         .replace("bounced", "" ) 
x = open("output.csv","w")
x.writelines(text)
x.close()