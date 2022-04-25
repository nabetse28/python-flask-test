from flask import Flask
from flask_restx import Api
from api.v1.person.controller.person import NS_PERSON
from api.v1.status.controller.status import NS_STATUS

app = Flask(__name__)
api = Api(app=app, version="0.0")

api.add_namespace(NS_STATUS)
api.add_namespace(NS_PERSON)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8005)
