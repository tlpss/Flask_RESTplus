from flask_restplus import Resource, Api

from app.routes.competitions_api_namespace import  api as competitions_api

api = Api()

@api.route('/')
class Test(Resource):
    def get(self):
        return {"test": "succeeded"}

api.add_namespace(competitions_api,"/api/competitions")


