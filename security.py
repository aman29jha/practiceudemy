from werkzeug.security import safe_str_cmp
from models.user import Usermodel

def authenticate(username, password):
    user = Usermodel.findbyusername(username)
    if user and safe_str_cmp(user.password, password) :
        return user

def identity(payload) :
    user_id = payload['identity']
    return Usermodel.findbyuserid(user_id)



