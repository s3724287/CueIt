from flask import Flask, render_template
import pandas as pd 
from csv import reader
import json 



app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/app')
def main():
   return render_template('app.html')




if __name__ == '__main__':
   
   app.run()