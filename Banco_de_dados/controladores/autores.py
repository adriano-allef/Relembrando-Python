from flask import Flask, make_response, jsonify
from bancodedados import autores_repo

def autores():
    autores = autores_repo.listar_todos()
    return make_response(jsonify(autores))
