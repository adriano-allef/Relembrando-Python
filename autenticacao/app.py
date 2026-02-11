from flask import Flask
from controladores import usuarios

app = Flask(__name__)

app.add_url_rule('/cadastro', methods= ['POST'], view_func=usuarios.cadastrar)

app.run(port=3000, debug=True)