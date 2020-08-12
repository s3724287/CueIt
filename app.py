from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import pandas as pd 
import numpy as np
from csv import reader
import pandas
from werkzeug.utils import secure_filename
import json 
import pandas.io.excel._openpyxl
import tempfile
import os
#
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'xlsx', 'csv'}
#
app = Flask(__name__, static_url_path="/static")
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
#
@app.route('/')
def index():
    return render_template('index.html')
#
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
#
@app.route('/pricing')
def pricing():
   return render_template('pricing.html')
#
@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')
#
@app.route('/login')
def logIn():
    return render_template('login.html')
#
@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
#
@app.route('/privacy')
def privacy():
   return render_template('privacy.html')
#
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
@app.route('/app', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename, )
            
    return render_template('app.html')
#
def process_file(path, filename):
    prep_cue(path, filename)       
#
def prep_cue(path, filename):
    # REPLACING CHARS & CLEAING UP MUSIC CUE SHEET UPLOAD FOR NLP TO ANALYSE
    input_file = pandas.read_excel(path)
    input_file['trackTitle'] = input_file['trackTitle'].str.replace('_', ' ')
    input_file['trackTitle'] = input_file['trackTitle'].str.replace('.WAV', ' ')
    input_file['trackTitle'] = input_file['trackTitle'].str.replace('.new', ' ')
    input_file['trackTitle'] = input_file['trackTitle'].str.replace('.01', ' ')
    input_file['trackTitle'] = input_file['trackTitle'].str.replace('Bounced', ' ')
    #
    #input_file["duration"].fillna("00:00:00:00", inplace = True)
    
    input_file.to_csv(app.config['DOWNLOAD_FOLDER'] + 'processed_file')
    
  


























@app.route('/uploads/<filename>')
def uploaded_file():
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], processed_file, as_attachment=True)
#
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
