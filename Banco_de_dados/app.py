from flask import Flask
from controladores import autores

app = Flask(__name__)

app.add_url_rule('/autor', view_func=autores.autores)


app.run(port=3000, debug=True, host='localhost')