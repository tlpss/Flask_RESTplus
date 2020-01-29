from flask_restplus import Namespace, Resource, fields
from app.models.competition import Competition
from app import db

api = Namespace('competition',description="competitions related operations")

# return marshalling model
competition_model = api.model('Competition', {
    'id': fields.Integer(required=True, description="Unique identifier"),
    'name': fields.String(required=True, description = "verbose identifier")
})

# request parser

competition_parser = api.parser()
competition_parser.add_argument('name', type=str,required=True,help='name of the new competition')

@api.route('/')
class CompetitionsList(Resource):
    @api.doc('List competitions')
    @api.marshal_list_with(competition_model)
    def get(self):
        list = Competition.query.all()
        print(len(list))
        return list

    @api.expect(competition_parser)
    def post(self):
        args = competition_parser.parse_args()
        c = Competition(name=args.get('name'))
        db.session.add(c)
        db.session.commit()
