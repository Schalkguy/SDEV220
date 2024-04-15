from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
app = Flask(__name__)

#Module 4 API assignment
#4/15/2024

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model): #Create book in sql
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f"{self.name} - by {self.author}"

@app.route('/') #Homepage
def index():
    return 'Hello!'

@app.route('/books') #list of books
def get_books():
    books = Book.query.all()

    output = []
    for book in books: output.append({'name':book.name, 'author':book.author, 'publisher':book.publisher})

    return {"Books":output}

@app.route('/books/<id>') #Get book info by id
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name':book.name, 'author':book.author, 'publisher':book.publisher}

@app.route('/books', methods=['Post']) #Add book
def add_book():
    book = Book(name=request.json['name'], author=request.json['Author'], publisher=request.json['Publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}

@app.route('/books,<id>', methods=['DELETE']) #Delete book
def delete_book():
    book = Book.query.get(id)
    if book is None: #Entered book ID does not exist
        return{"error": 404}
    db.session.delete(book)
    db.session.delete(book)
    return{"message": 200}

#NOTE TO SELF CONSOLE COMMANDS
# set FLASK_APP=book_api.py
#$env:FLASK_APP = "book_api.py"

#ANNOYING
#>>> from books import app, db   
#>>> app.app_context().push()

#db.session.add()
#db.session.commit()