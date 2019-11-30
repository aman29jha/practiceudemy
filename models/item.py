from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # foreign key linkage wih store table
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name,price):
        self.name = name
        self.price = price
    def json(self):
        return{'name' : self.name, 'price': self.price}
    def savetodb(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def findbyitemname(cls, name):
        return cls.query.filter_by(name = name).first()




