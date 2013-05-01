from google.appengine.ext import db


class User(db.Model):
    name = db.StringProperty(required=True)
    username = db.StringProperty()
    password = db.StringProperty()
    doe = db.DateTimeProperty(auto_now_add=True)
    dou = db.DateTimeProperty(auto_now=True)

    @staticmethod
    def get_by_username(username):
        return User.gql("WHERE username = :usr", usr=username)
