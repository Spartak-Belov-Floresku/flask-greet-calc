from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcomeFank():
    return 'welcome'


@app.route('/welcome/home')
def welcomeHomeFank():
    return 'welcome home'


@app.route('/welcome/back')
def welcomeBackFank():
    return 'welcome back'
