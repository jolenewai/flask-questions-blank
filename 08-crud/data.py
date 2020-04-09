import csv

def read_books():
    fp = open('books.csv', 'r', newline='\n')
    reader = csv.reader(fp, delimiter=",")
    next(reader)

    database = []

    for each_book in reader:
        book = {
            each_book[1]:{
                "isbn": each_book[0], 
                "author": each_book[2],
                "year_published": each_book[3]
                }
        }
        # print(book)
        database.append(book)

    fp.close()
    return database

def list_book():
    library = read_books()
    # print(library)
    book_titles = []
    for book in library:
        for key,value in book.items():
            book_titles.append({
                'title':key,
                'isbn':value['isbn']
            })

    print(book_titles)        
    return book_titles

def find_book(query):
    books = list_book()
    book_found = []
    for each_book in books:
        print(each_book)
        if each_book['title'].lower().find(query.strip().lower()) >= 0:
            book_found.append(each_book['title'])
            
    return book_found

def add_book(title, isbn, author, year_published):

    current_library = read_books()

    for each_book in current_library:
        print (each_book)
        # for key,value in each_book.items():
            # if isbn == each_book[isbn]
            #     isbn_exist = True
            #     break
            # else:
            #     isbn_exist = False

    # new_book = {
    #     title:{
    #         "isbn":isbn,
    #         "author": author,
    #         "year_published": year_published
    #     }
    # }

    # if isbn_exist == False:
    #     with open('books.csv','a') as fp:
    #         writer = csv.writer(fp, delimiter=",")
    #         writer.writerow(new_book)
    #     message="Book added"            
    # else:
    #     message = "ISBN exists. Book not added"

    message = ""    
    return message

def get_book_by_isbn(isbn):
    current_library = read_books()

    for each_book in current_library:
        for key,value in each_book.items():
            if isbn == value[0]:
                return each_book
                break

    return book_found


def modify_book(title, isbn, author, year_published):
    book_to_update = get_book_by_isbn(isbn)
    
    current_library = read_books()
    new_library = []

    for each_book in current_library:
        # for key,value in each_book.items():        
        if each_book['isbn'] == isbn:
            each_book['title'] = title
            each_book['author'] = author
            each_book['year_published'] = year_published

        new_library.append(each_book)    

    print (new_library)
    # with open('books.csv','w') as fp:
    #     writer = csv.writer(fp,delimiter(','))
    #     writer.writerow(['ISBN','title','author','year_published'])

    #     for each_book in new_library:
    #         write.writerow(each_book)



    





