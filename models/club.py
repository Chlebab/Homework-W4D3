from app import db

class Club(db.Model):
    __tablename__ = "clubs"
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(64))
    players = db.relationship('Player', backref='club')
    def __repr__(self):
        return f"<Club {self.id}: {self.club}>" 
    