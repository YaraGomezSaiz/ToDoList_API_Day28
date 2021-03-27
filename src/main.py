"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Todos
from json_helper import jsonify_array
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    users=User.query.all()
    users_dict = []
    for user in users:
        users_dict.append(user.serialize)

    print(users_dict)
    return jsonify(users_dict), 200

# GET todas las tareas del modelo Todos
@app.route('/todos', methods=['GET'])
def getTodos():
    
    tasks=Todos.get_all()
    return jsonify_array(tasks), 200
   
# POST- Crear una tarea nueva en la tabla Todos
@app.route('/todos', methods=['POST'])
def postTodos():

    # body=request.get_json()
    # todo= Todos(body["label"], body["is_done"])
    # todo.set_body(body)
    todo=Todos.set_body(request.get_json())

    
    # body=request.get_json()
    # todo=Todos()

    # # todo.id=body["id"]
    # todo.label=body["label"]
    # todo.is_done=body["is_done"]

    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.serialize()),200

@app.route('/todos/<int:id>', methods=['PUT'])
def updateTodo(id):
    
    body=request.get_json()
    todo = Todos.query.get(id)
    todo.label=body["label"]

    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.serialize()),200


    
@app.route('/todos/<int:id>', methods=['DELETE'])
def deleteTodo(id):
    
    todo = Todos.query.get(id)
    
    db.session.delete(todo)
    db.session.commit()

    return jsonify(todo.serialize()),200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
