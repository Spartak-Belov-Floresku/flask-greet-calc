from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_fank():
    return 'welcome'


@app.route('/welcome/home')
def welcomeHome_fank():
    return 'welcome home'


@app.route('/welcome/back')
def welcome_back_fank():
    return 'welcome back'
