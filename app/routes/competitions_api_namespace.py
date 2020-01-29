from flask_restplus import Namespace, Resource, fields, abort
from app.models.competition import Competition
from app import db

api = Namespace('competition',description="competitions related operations")

# return marshalling model
competition_model = api.model('Competition', {
    'id': fields.Integer(required=True, description="Unique identifier"),
    'name': fields.String(required=True, description = "verbose identifier")
})

# post request parser

competition_post_parser = api.parser()
competition_post_parser.add_argument('name', type=str, required=True, help='name of the new competition')

# post get search param parser

competition_get_parser = api.parser()
competition_get_parser.add_argument('name', type=str, required=False, help='optional: name of the  competition ')
@api.route('/')
class CompetitionsList(Resource):
    @api.doc('List competitions')
    @api.marshal_list_with(competition_model)
    def get(self):
        list = Competition.query.all()
        print(len(list))
        return list

    @api.expect(competition_post_parser)
    def post(self):
        args = competition_post_parser.parse_args()
        if Competition.query.filter_by(name=args.get('name')).scalar() is not None:
            abort(422,"name already exists")

        c = Competition(name=args.get('name'))
        db.session.add(c)
        db.session.commit()
        # create response
        result = api.marshal(c,competition_model)
        return result, 200
