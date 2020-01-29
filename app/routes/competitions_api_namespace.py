from flask_restplus import Namespace, Resource, fields
from app.models.competition import Competition
from app import db

api = Namespace('competition',description="competitions related operations")

competition_model = api.model('Competition', {
    'id': fields.Integer(required=True, description="Unique identifier"),
    'name': fields.String(required=True, description = "verbose identifier")
})

@api.route('/')
class CompetitionsList(Resource):
    @api.doc('List competitions')
    @api.marshal_list_with(competition_model)
    def get(self):
        list = Competition.query.all()
        print(len(list))
        return list

    def put(self):
        c = Competition(name="test")
        db.session.add(c)
        db.session.commit()
