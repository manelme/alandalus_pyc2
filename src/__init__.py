# coding: utf-8

import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("hs.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r',encoding="utf8") as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class Institutos(Resource):
    
        def get(self):
                shelf = get_db()
                keys = list(shelf.keys())

                institutos = []

                for key in keys:
                        institutos.append(shelf[key])

                return {'message': 'Success', 'data': institutos}, 200

        def post(self):
                parser = reqparse.RequestParser()

                parser.add_argument('id', required=True)
                parser.add_argument('nombre', required=True)
                parser.add_argument('codigo', required=True)
                parser.add_argument('fax', required=True)
                parser.add_argument('web', required=True)

                # Parse the arguments into an object
                args = parser.parse_args()

                shelf = get_db()
                shelf[args['id']] = args

                return {'message': 'Instituto registered', 'data': args}, 201

class Instituto(Resource):
        def get(self, id):
                shelf = get_db()

                # If the key does not exist in the data store, return a 404 error.
                if not (id in shelf):
                        return {'message': 'Instituto not found', 'data': {}}, 404

                return {'message': 'Instituto found', 'data': shelf[id]}, 200

        def delete(self, id):
                shelf = get_db()

                # If the key does not exist in the data store, return a 404 error.
                if not (id in shelf):
                        return {'message': 'Instituto not found', 'data': {}}, 404

                del shelf[id]
                return '', 204


api.add_resource(Institutos, '/instituto')
api.add_resource(Instituto, '/instituto/<id>')
