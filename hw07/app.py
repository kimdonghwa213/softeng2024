from flask import Flask, render_template

App = Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/career')
def career():
    return render_template('career.html')

@App.route('/about_me')
def about_me():
    return render_template('about_me.html')

App.run(debug=True)