from app import db

class Competition(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(256),unique=True)
    teams = db.relationship('Team',backref = "competition", lazy = "dynamic")
    def __repr__(self):
        return f"<Competition {self.id} - {self.name}"


