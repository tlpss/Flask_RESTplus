from app import db

class Player(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=False)
    team_id = db.Column(db.Integer,db.ForeignKey('team.id'))