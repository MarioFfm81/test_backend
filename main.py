from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required, JWTError
from resources.feedback import Feedback

from security import authenticate, indentity

app = Flask(__name__)
app.secret_key = "das ist mein eigener test"


api = Api(app)
jwt = JWT(app, authenticate, indentity)

api.add_resource(Feedback, '/feedback')

if __name__=='__main__':
    app.debug=True
    app.run()