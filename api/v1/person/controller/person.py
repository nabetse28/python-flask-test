from flask_restx import Resource, Namespace
from flask import request

NS_PERSON = Namespace(name="Person", description="This is the status check of the app", path="/api")


@NS_PERSON.route("/v1/person")
class Person(Resource):
    @NS_PERSON.response(code=200, description="Success")
    @NS_PERSON.response(code=404, description="Not found")
    @NS_PERSON.response(code=500, description="Internal server error")
    def post(self):

        data = request.json()

        return {"message": "All persons"}, 200


@NS_PERSON.route("/v1/person/<string:name>")
class PersonGetById(Resource):
    @NS_PERSON.response(code=200, description="Success")
    @NS_PERSON.response(code=404, description="Not found")
    @NS_PERSON.response(code=500, description="Internal server error")
    def get(self, name):
        return {"message": "A person"}, 200

    @NS_PERSON.response(code=200, description="Success")
    @NS_PERSON.response(code=404, description="Not found")
    @NS_PERSON.response(code=500, description="Internal server error")
    def delete(self, name):
        return {"message": "A person"}, 200

    @NS_PERSON.response(code=200, description="Success")
    @NS_PERSON.response(code=404, description="Not found")
    @NS_PERSON.response(code=500, description="Internal server error")
    def put(self, name):
        return {"message": "A person"}, 200
