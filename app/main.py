from app.model.book import BookDAO
from app.services.book_service import *
from flask import Flask, jsonify, Blueprint, request
from flask_restx import Api, Resource, fields
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
main = Blueprint("/", __name__, template_folder='templates',static_folder='static')
api = Api(app, version='1.0', title='Literary Works API', description='Python API study project',)
ns = api.namespace('books', description='Literary works')

BOOK_API_MODEL = api.model('Book', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'author_full_name': fields.String(required=True, description='The task details'),
    'book_name': fields.String(required=True, description='The task details'),
    'genre': fields.String(required=True, description='The task details'),
    'first_publication_date': fields.Integer(required=True, description='The task details'),
    'total_page_number': fields.Integer(required=True, description='The task details'),
})

DAO = BookDAO()

###
# This class gets a list of objects
@ns.route('/')
class BookList(Resource):
    '''Shows a list of all books'''
    @ns.doc('list_books')
    @ns.marshal_list_with(BOOK_API_MODEL)
    def get(self):
        '''List all books'''
        return get_books()


    @ns.doc('create_book')
    @ns.expect(BOOK_API_MODEL)
    @ns.marshal_with(BOOK_API_MODEL, code=201)
    def post(self):
        '''Create a new entry'''
        return DAO.create(api.payload), 201

###
# This class works with one object
@ns.route('/<int:id>')
@ns.response(404, 'Book not found')
@ns.param('id', 'Book ID')
class Book(Resource):
    '''Show a single book entry'''
    @ns.doc('get_book')
    @ns.marshal_with(BOOK_API_MODEL)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_book')
    @ns.response(204, 'Book deleted')
    def delete(self, id):
        '''Delete a book given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(BOOK_API_MODEL)
    @ns.marshal_with(BOOK_API_MODEL)
    def put(self, id):
        '''Update a book given its identifier'''
        return DAO.update(id, api.payload)

###
# Sorting
@ns.route('/sortby')
@ns.doc(params={'author': {'description': 'set true if needs to be sorted by', 'in': 'query', 'type': 'boolean'},
'title': {'description': 'set true if needs to be sorted by', 'in': 'query', 'type': 'boolean'},
'genre': {'description': 'set true if needs to be sorted by', 'in': 'query', 'type': 'boolean'},
'first-publication-date': {'description': 'set true if needs to be sorted by', 'in': 'query', 'type': 'boolean'},
'total-page-number': {'description': 'set true if needs to be sorted by', 'in': 'query', 'type': 'boolean'},
'sort_order': {'description': 'Possible values: asc, desc. Default is ascending sort', 'in': 'query', 'type': 'string'}})
class MyResource(Resource):
    def get(self):
        '''Sort by parameters (look inside for more detail)'''
        author_sort = request.args.get('author')
        title_sort  = request.args.get('title')
        genre_sort  = request.args.get('genre')
        date_sort  = request.args.get('first-publication-date')
        page_sort  = request.args.get('total-page-number')
        sort_order = request.args.get('sort_order')
        return get_books_sorted(author_sort, title_sort, genre_sort, date_sort, page_sort, sort_order)


@ns.route('/avgdate')
class BookAvgDate(Resource):
    @ns.doc('list_avg_date')
    def get(self):
        '''Shows average value of all first publication dates (year only)'''
        return get_avg_date()
         
@ns.route('/avgpage')
class BookAvgPage(Resource):
    @ns.doc('list_avg_page')
    def get(self):
        '''Shows average value of all page totals'''
        return get_avg_page_number()

@ns.route('/mindate')
class BookMinDate(Resource):
    @ns.doc('list_min_date')
    def get(self):
        '''Shows mimimal value of all first publication dates (year only)'''
        return get_min_date()

@ns.route('/minpage')
class BookMinPage(Resource):
    @ns.doc('list_min_page')
    def get(self): 
        '''Shows minimal value of all page totals'''
        return get_min_page_number()

@ns.route('/maxdate')
class BookMaxDate(Resource):
    @ns.doc('list_max_date')
    def get(self):
        '''Shows maximum value of all first publication dates (year only)'''
        return get_max_date()

@ns.route('/maxpage')
class BookMaxPage(Resource):
    @ns.doc('list_max_page')
    def get(self):
        '''Shows maximum value of all page totals'''
        return get_max_page_number()

if __name__ == '__main__':
    app.run()