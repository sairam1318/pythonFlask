from flask import Flask;
from flask_restful import Api, Resource;

app = Flask(__name__)
api = Api(app)

names = {
    "sairam": {
        "Age": "24",
    },
    "jayasri": {
        "Age": "22"
    }
}
class Helloworld(Resource):
    def get(self, name):
        return names[name]
    # def post(self):
    #     return {'data': 'Jayasri'}
    
api.add_resource(Helloworld, '/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)