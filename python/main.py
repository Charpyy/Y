from flask import Flask, render_template, redirect, url_for, request
import pandas as pd

app = Flask(__name__)

users = pd.read_csv('User.csv')['user'].tolist()
passwords = pd.read_csv('User.csv')['password'].tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']

    # Vérifiez si les informations d'identification sont valides
    if user in users and passwords[users.index(user)] == password:
        return redirect(url_for('home'))
    else:
        return 'Invalid credentials'

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)