from flask import Flask
from controladores import autores

app = Flask(__name__)

app.add_url_rule('/', view_func=autores.teste)


app.run(port=3000, debug=True)