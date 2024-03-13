from flask import Flask
from flask_cors import CORS
from config import connection_db, test_connection_db
from controllers import controllers_db

app = Flask(__name__)
CORS(app, resources={r"/connection_db": {"origins": "http://localhost:3003"}}, supports_credentials=True)

# Registrar as rotas

app.register_blueprint(connection_db)
app.register_blueprint(test_connection_db)
app.register_blueprint(controllers_db)

if __name__ == "__main__":
    # Roda o aplicativo em modo de depuração na porta 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
