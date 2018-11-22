from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required, JWTError
from resources.feedback import Feedback
import admin.startup
from applicationinsights.flask.ext import AppInsights

from resources.security import authenticate, indentity

app = Flask(__name__)
app.secret_key = "das ist mein eigener test"
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '624b7480-cc70-449f-ac63-60410783b680'
appinsights = AppInsights(app)


api = Api(app)
jwt = JWT(app, authenticate, indentity)

api.add_resource(Feedback, '/')

if __name__=='__main__':
    app.debug=True
    app.run()