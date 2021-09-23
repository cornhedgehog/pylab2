import json
from flask_restx import api

DB_PATH = 'app/model/database.json'
   
class BookDAO(object):
    def __init__(self):
        self.author_full_name = ""
        self.book_name = ""
        self.genre = ""
        self.first_publication_date = 0
        self.total_page_number = 0
        self.books = open_db()
        self.counter = len(self.books)

    def get(self, id):
        for book in self.books:
            if book['id'] == id:
                return book
        api.abort(404, "Book {} doesn't exist".format(id))

    def create(self, data):
        book = data
        book['id'] = self.counter = self.counter + 1
        self.books.append(book)
        self.update_db()
        return book

    def update(self, id, data):
        book = self.get(id)
        if not book:
            api.abort(404, "Book {} doesn't exist".format(id))
        book.update(data)
        self.update_db()
        return book

    def delete(self, id):
        book = self.get(id)
        if not book:
            api.abort(404, "Book {} doesn't exist".format(id))
        self.books.remove(book)
        self.update_db()

    def update_db(self):
       out_file = open(DB_PATH, "w")
       json.dump(self.books, out_file)
       out_file.close()

def open_db():
    f = open(DB_PATH)
    result = json.load(f)
    f.close()
    return result

def get_list():
    return open_db()
    