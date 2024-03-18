from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/delete-all')
def delete_all():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Ajoutez des données à la base dedonnées ici si vous le souhaitez
        new_book = Book(title="1984", author="George Orwell")
        db.session.add(new_book)
        db.session.commit()
        app.run(debug=True)