from flask import Blueprint, request, jsonify
from Project import db
from Project.Users.models import Usuario
from Project.Users.serializers import Usuario_Schema
from marshmallow.exceptions import ValidationError

user_blueprint = Blueprint('users', __name__)


def save_user(user):
    db.session.add(user)
    db.session.commit()



@user_blueprint.route('/register', methods=['POST'])
@user_blueprint.route('/users', methods=['POST'])
def CreateUser():
  user = Usuario_Schema.load(request.get_json())

  save_user(user)

  return Usuario_Schema.dump(user), 201



@user_blueprint.route('/users', methods=['GET'])
def list():
    users = Usuario.query.all()

    return jsonify (Usuario_Schema.dump(users, many=True)), 200



@user_blueprint.route('/users/<id>', methods=['GET'])
def view(id):
    user = Usuario.query.filter_by(id=id).first()

    return {'id': user.id, 'nombre': user.nombre, 'correo': user.correo, 'direccion': user.direccion}, 200


@user_blueprint.route ('/users/<id>', methods=['DELETE'])
def delete(id):

    user = Usuario.query.get_or_404(id)

    db.session.delete(user)   
    db.session.commit()

    return '', 204 


@user_blueprint.route ('/users/<id>', methods=['PUT'])
def update(id):

    user = Usuario.query.filter_by(id=id).first()
    datos = request.get_json()

    user.nombre = datos['nombre']
    user.correo = datos['correo']
    user.direccion = datos['direccion']

    save_user(user)

    return {'id': user.id, 'nombre': user.nombre, 'correo': user.correo, 'direccion': user.direccion}, 200