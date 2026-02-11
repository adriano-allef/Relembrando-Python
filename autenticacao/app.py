from flask import Flask

app = Flask(__name__)

@app.route('/')
def teste():
    return 'hello world'

app.run(port=3000, debug=True)