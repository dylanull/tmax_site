from flask import Flask, request, render_template
import pandas

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/select-file')
def select_file():
    return render_template('select-file.html')

@app.route('/tmx')
def tmx_spreadsheet():
    file = "source/tmax.xlsx"
    data = pandas.read_excel(file)
    return data.to_html()

@app.route('/src')
def src_spreadsheet():
    file = "source/src.xlsx"
    data = pandas.read_excel(file)
    return data.to_html()

@app.route('/cic')
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