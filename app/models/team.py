from app import db


class Team(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(256),unique=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))
    players = db.relationship('Player', backref="team", lazy="dynamic")