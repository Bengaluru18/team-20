from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


class Events(Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str)
        parser.add_argument('num', type=str)
        args = parser.parse_args()

        print (args)
        return "Hello {}".format(args["name"])


api.add_resource(Events, "/api/hello")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
