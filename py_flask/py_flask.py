#-*-coding:utf-8 -*-
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<name>')
def api_test_report(name):
    if str(name).upper() == 'API':
        return render_template('Api_wc.html',name=name)
    elif str(name).upper() == 'GUI':
        return render_template('Gui_wc.html',name=name)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
