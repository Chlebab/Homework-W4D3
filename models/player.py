from app import db

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    position = db.Column(db.String(64))
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))

    def __repr__(self):
        return f"<Player: Id: {self.id}, name: {self.name}, age: {self.age}, position: {self.position}, club_id:{self.club_id}>"