from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas, sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/select-file')
def select_file():
    return render_template('select-file.html')

@app.route('/tmx')
def search_tmx():
    return render_template('tmx.html')

@app.route('/src')
def search_src():
    return render_template('src.html')

@app.route('/cic')
def search_cic():
    return render_template('cic.html')


#### Spreadsheet Views
@app.route('/tmx_spreadsheet')
def tmx_spreadsheet():
    file = "source/tmax.xlsx"
    data = pandas.read_excel(file)
    return data.to_html()

@app.route('/src_spreadsheet')
def src_spreadsheet():
    file = "source/src.xlsx"
    data = pandas.read_excel(file)
    return data.to_html()

@app.route('/cic_spreadsheet')
def cic_spreadsheet():
    file = "source/cic.xlsx"
    data = pandas.read_excel(file)
    return data.to_html()

if __name__ == "__main__":
    app.run()



#@app.route('/list-view')
#def list_view():
#    file = "source/tmax.xlsx"
#    data = pandas.read_excel(file)
#    return data.to_html()