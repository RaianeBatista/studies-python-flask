from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_wold():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)