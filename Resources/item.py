from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource) :
    TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    @jwt_required()
    def get(self, name):
        item = ItemModel.findbyitemname(name)
        if item :
            return item.json()
        else :
            return {"Item not found"}

    def post(self, name):
        data = Item.parser.parse_args()
        x = ItemModel.findbyitemname(name)
        if x is not None :
            return {'message': "An item with name '{}' already exists.".format(name)}
        else :
            item = ItemModel(name, **data)
            item.savetodb()
        return item.json()

    @jwt_required()
    def delete(self, name):
        x = ItemModel.findbyitemname(name)
        if x is not None :
           x.delete()
           return {"the item has been deleted"}
        return {"item not found"}

    def put(self, name):
        data = Item.parser.parse_args()
        x = ItemModel.findbyitemname(name)
        y = x.json()
        if y.get("name") is not None :
            x.price = data['price']
            return {'message': "An item with name '{}' already exists."}
        else :
            x = ItemModel(name, **data)
        x.savetodb()
        return {"items modified"}

class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}