from flask import Flask, request, jsonify
import ABB, csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'respuesta':'done'}),200
'''
@app.route('/saludar/<nombre>', methods=['GET'])
def saludar(nombre):
    return f'Hola, {nombre}!'''

#----------------------------------------------
@app.route('/show/<user_id>', methods=['GET'])
def show(user_id):
    user = {"id" : user_id, "name": "test", "telefono": "58513753"}
    query  = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    data["status"] = 'user crated'
    return jsonify(data), 201



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)