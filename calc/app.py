# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_num():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def sub_num():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def mult_num():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def div_num():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

@app.route('/math/<domath>')
def math_func(domath):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(eval(domath)(a,b))
