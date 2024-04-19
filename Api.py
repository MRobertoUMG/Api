from flask import Flask, request, jsonify
import ABB, csv

from flask_restful import Resource, Api

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
def show(user_id):sd
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

@app.route('/upload', methods=['POST'])
def upload():
    class UploadCSV(Resource):
        def post(self):
            file = request.files['file']
            if file:
                filename = secure_filename(file.filename)
                file.save(filename)
                return {'message': 'File uploaded successfully'}, 201
            else:
                return {'error': 'No file uploaded'}, 400
#api.add_resource(UploadCSV, '/upload')

@app.route('/team', methods=['GET'])
def team():
    team = {{"nombre" : "Mario Roberto Rompich Yoc", "carnet": "9490-17-17052", "Contribucion": "100%", "nombre" : "Mario Roberto Rompich Yoc", "carnet": "9490-17-17052", "Contribucion": "100%"}}
    query  = request.args.get('query')
    if query:
        team["query"] = query
    return jsonify(team), 200
 




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)