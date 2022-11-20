'''Code for flask'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    '''Code for flask'''
    return "Hello World!"

@app.route('/status')
def status():
    '''Code for flask'''
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)