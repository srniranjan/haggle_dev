from google.appengine.ext import db

class User(db.Model):
    email = db.StringProperty()
    name = db.StringProperty(indexed=False)
    password = db.StringProperty(indexed=False)
    force_reset_password = db.BooleanProperty(indexed=False)
    total_checkins = db.FloatProperty(indexed=False)
    total_friends = db.IntegerProperty(indexed=False)
    total_followers = db.IntegerProperty(indexed=False)
    last_updated_pipeline = db.StringProperty(indexed=False)

    @classmethod
    def get_or_insert(cls, key_name, **kwds):
        kwds['email'] = key_name
        return super(User, cls).get_or_insert(key_name, **kwds)

    @property
    def friends_followers_count(self):
        return (self.total_friends or 0) +  (self.total_followers or 0)

    @staticmethod
    def get_by_email(email):
        return User.get_by_key_name(email)


