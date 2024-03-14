from flask import Flask, render_template, send_from_directory , flask_sqlalchemy
import os

app = Flask(__name__)
css_dir = os.path.join(os.path.dirname(__file__), 'css')


@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(css_dir, filename)


@app.route('/')
def acc():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)