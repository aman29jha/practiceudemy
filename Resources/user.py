import sqlite3
from flask_restful import Resource,reqparse
from models.user import Usermodel
class UserRegister(Resource):
    TABLE_NAME = 'users'
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    def post(self):
        data = UserRegister.parser.parse_args()
        if Usermodel.findbyusername(data['username']) is not None :
            return {'message': "An user with name '{}' already exists."}
        else :
            x = Usermodel(data['username'], data['password'])
            x.insert()
            return {"user has been created"}







