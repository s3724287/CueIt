from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import pandas as pd 
from csv import reader
import pandas
from werkzeug.utils import secure_filename
import json 
import os
#
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'xlsx'}
#
app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
#
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return redirect(request.url)
    return render_template('app.html')
#
#@app.route('/', methods=['GET', 'POST'])
#def index():
#    if request.method == 'POST':
#        if 'file' not in request.files:
#            print('No file attached in request')
#            return redirect(request.url)
#        df1 = pd.read_csv(request.files('file'))
#        file = request.files['file']
#        if file.filename == '':
#            print('No file selected')
#            return redirect(request.url)
#        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
#            return redirect(url_for('uploaded_file', filename=filename))
#    return render_template('app.html')
#
@app.route('/app')
def application():
   return render_template('app.html')
#
#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/sign-up')
def singUp():
    return render_template('sign-up.html')
#
@app.route('/log-in')
def logIn():
   return render_template('log-in.html')
#
@app.route('/pricing')
def pricing():
   return render_template('pricing.html')
#  
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_cue(path, filename):
     process_cue(path, filename)
#
def process_cue(file, filename):
    df1 = pd.read_csv(request.files('file'))
    df1.replace(to_replace = ["copy.01.new.01", "bounced", ".wav", ".", "aiff", "Bounce", "new 01", "WAV", "wav", ".new", "AIF"],
                              value = " ")
#
#df1.to_excel(app.config['UPLOAD_FOLDER'] + filename)
   
   
   
   #text = open(path, 'r', encoding='latin-1')
   #text = ''.join([i for i in text]).replace("_", " ") \
   #      .replace("copy.01.new.01", " " ) \
   #      .replace("bounced", " " ) \
   #      .replace(".wav", " " ) \
   #      .replace(".", " " ) \
   #      .replace("aiff", " ") \
   #      .replace("Bounce", " ")\
   #      .replace("new 01", "")\
   #      .replace("WAV", "")\
   #      .replace("wav", "")\
   #      .replace(".new", "") \
   #      .replace("AIF", "")
   #y = open(app.config['UPLOAD_FOLDER'] + output, 'w')
   #y.writelines(text)
   #
  # fincolnames = ['trackTitle', 'duration', 'trackNumber', 'trackID']
  # finalData = pandas.read_csv(path, names=fincolnames, skiprows=[0], usecols=['trackTitle', 'duration', 'trackNumber', 'trackID',])
   #
  # finalData1 = pandas.DataFrame(columns=['composer', 'record-label', 'publisher', 'hr', 'min', 'sec', 'frames'], index=finalData.index )
   #
  # libcolnames = ['PREFIX', 'LABEL', 'PUBLISHER']
 #  data = pandas.read_csv('MusicLibraries.csv', names=libcolnames, skiprows=[0])
   #
  # finalData["duration"].fillna("00:00:00:00", inplace = True)
   #
  # for d in range(len(finalData)):
  #    finalData1['hr'][d], finalData1['min'][d], finalData1['sec'][d], finalData1['frames'][d] = str(finalData['duration'][d]).split(":")
   #
  # for e in range(len(finalData)):
   #     me = finalData['trackID'][e]
  # for i in range (len(data['PREFIX'])):
   #     if re.match(str(data['PREFIX'][i]), str(me)):     
   #      finalData1['record-label'][e] = (str(data['LABEL'][i]))
   #      finalData1['publisher'][e] = (str(data['PUBLISHER'][i]))
   #
   #dataExport = finalData.append(finalData1)


@app.route('/uploads/<filename>', endpoint="sectors")
def uploaded_file(filename):
   return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)
#
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)

