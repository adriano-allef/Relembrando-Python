from flask import make_response, jsonify, request
from bancodedados import usuarios_repository

def cadastrar():
    body = request.get_json()

    existe_email = usuarios_repository.buscar_email(body['email'])

    if existe_email != None:
        return make_response({'Mensagem': 'Já existe um usuário com o email informado'}, 400)

    usuario = usuarios_repository.cadastrar(body['nome'], body['email'], body['senha'])

    return make_response(jsonify(usuario), 201)
