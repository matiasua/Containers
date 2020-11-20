from flask import Blueprint, request, jsonify
from Project import db
from Project.Users.models import Usuario
from Project.Users.serializers import Usuario_Schema, login_Schema
from marshmallow.exceptions import ValidationError

user_blueprint = Blueprint('users', __name__)


def save_user(user):
    db.session.add(user)
    db.session.commit()



@user_blueprint.route('/register', methods=['POST'])
def CreateUser():
    datajson = request.get_json()
    if datajson != {}:
        if datajson['password'] == datajson['confirmPassword']:
            user = Usuario_Schema.load(request.get_json())

            save_user(user)

            return "Registro Exitoso", 201
        return "Error de contraseña", 400
    return "Campos Vacios", 400


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


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    loginObject = login_Schema.load(request.get_json())
    user_query = Usuario.query.filter_by(correo=loginObject.correo).first()

    if user_query != None:
        if user_query.password == loginObject.password:
            user = Usuario.query.filter_by(correo=loginObject.correo)
            return jsonify(Usuario_Schema.dump(user, many=True)), 200
        return "Contrasena incorrecta", 400
    return "Usuario no registrado", 400