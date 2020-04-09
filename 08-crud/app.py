from flask import Flask, render_template, request, redirect, url_for
import os
import data

app = Flask(__name__)

@app.route('/')
def index():
    library = data.list_book()
    # library = data.read_books()
    #print(library)
    return render_template('home.template.html', library = library)

@app.route('/search')
def search_form():
    return render_template('search.template.html')

@app.route('/search', methods=["POST"])
def process_search():
    query = request.form.get('search_query')
    book_found = data.find_book(query)
    return render_template('search.template.html', book=book_found)

@app.route('/add')
def add():
    return render_template('add_book.template.html')

@app.route('/add',methods=['POST'])
def process_add():
    title = request.form.get('title')
    isbn = request.form.get('isbn')
    author = request.form.get('author')
    year_published = request.form.get('year_published')
    message = data.add_book(title,isbn,author,year_published)
    return render_template('add_book.template.html', message=message)

@app.route('/edit/<isbn>')
def modify(isbn):
    book_info = data.get_book_by_isbn(isbn)
    return render_template('modify_book.template.html', book_info=book_info)

@app.route('/edit/<isbn>', methods=["POST"])
def process_modify(isbn):
    
    title = request.form.get('title')
    author = request.form.get('author')
    year_published = request.form.get('year_published') 

    data.modify_book(title,isbn,author,year_published)     
    # print(current_library)
    message = 'Book info updated'
    
    return render_template('modify_book.template.html',message=message)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)