# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def addNum():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def subNum():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def multNum():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def divNum():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

@app.route('/math/<domath>')
def mathFunc(domath):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(eval(domath)(a,b))
