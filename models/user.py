from db import db

class Usermodel(db.Model) :
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findbyusername(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def findbyuserid(cls, _id):
        return cls.query.filter_by(id = _id).first()

