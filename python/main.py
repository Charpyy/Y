from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
css_dir = os.path.join(os.path.dirname(__file__), 'css')


@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(css_dir, filename)


@app.route('/')
def acc():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)