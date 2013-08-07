import json

from google.appengine.ext import db

class JsonProperty(db.TextProperty):
    def validate(self,  value):
        return value
        
    def get_value_for_datastore(self,  model_instance):
        result =  super(JsonProperty,  self).get_value_for_datastore(model_instance)
        result =  json.dumps(self.to_json(result))
        return db.Text(result)

    def make_value_from_datastore(self,  value):
        return json.loads(str(value)) if value else None

    def to_json(self, result):
        return result
