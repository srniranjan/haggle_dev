from google.appengine.ext import db
import random
from model.location import Location
from model.category import Category
# from model.week_hours import WeekHoursProperty, WeekHours
# from util import clock

# DEFAULT_RATING = 1
# ALWAYS_OPEN = "00:00-23:30"
# ALWAYS_CL0SED = "00:00-00:00"
# class Vendor(db.Model):
#     name = db.StringProperty(indexed=False)
#     category = db.ReferenceProperty(Category)
#     vendor_location = db.ReferenceProperty(Location)
#     _operating_hours = WeekHoursProperty(indexed=False)
#     max_loyalty_score =  db.FloatProperty(indexed=False)
#     _dollar_rating =  db.IntegerProperty(indexed=False)
#     photo = db.StringProperty(indexed=False)
#     vendor_code = db.StringProperty(indexed=False)

#     category_name =  db.StringProperty(indexed=False)
#     location =  db.GeoPtProperty(indexed=False)
#     user_rating = db.FloatProperty(indexed=False)
#     neighborhoods =  db.StringListProperty(indexed=False)
#     phone_number = db.StringProperty(indexed=False)


#     @property
#     def dollar_rating(self):
#         return self._dollar_rating if self._dollar_rating else None

#     @dollar_rating.setter
#     def dollar_rating(self, value):
#         self._dollar_rating =  value

#     @property
#     def operating_hours_str(self):
#         return (self.operating_hours or WeekHours()).time_ranges_strs

#     @property
#     def city(self):
#         return self.vendor_location.city if self.vendor_location  else None

#     @property
#     def operating_hours(self):
#         return self._operating_hours or WeekHours.make_24_x_7()

#     @operating_hours.setter
#     def operating_hours(self, value):
#         self._operating_hours = value

#     @staticmethod
#     def generate_vendor_code():
#         return str(random.randint(0, 9999)).zfill(4)

#     @classmethod
#     def check_and_update_max_loyalty(cls, key, score):
#         if(cls.get(key).max_loyalty_score < score):
#             cls._check_and_update_max_loyalty(key, score)

#     @classmethod
#     @db.transactional
#     def _check_and_update_max_loyalty(cls, key, score):
#         vendor =  cls.get(key)
#         if(vendor.max_loyalty_score < score):
#             vendor.max_loyalty_score =  score
#             vendor.put()
#     @property
#     def id(self):
#         return self.key().id()

#     def json(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "code": self.vendor_code,
#             "operating_hours": self.operating_hours.time_ranges_strs,
#             "photo": self.photo
#         }

#     def local_datetime(self, time=None):
#         now = clock.eastern_datetime()
#         if time:
#             return clock.replace_time(now, time)
#         return now

#     def weekday(self):
#         return self.local_datetime().weekday()

#     def is_open(self, datetime_):
#         return self.operating_hours.is_datetime_in_range(datetime_)

#     def update(self, operating_hours = None, photo = None,
#                pin = None, name = None, dollar_rating = 0,  category = None,
#                neighborhoods = None, location = None, user_rating = 0.0,
#                category_name = None, phone_number = None):
#         if operating_hours:
#             self.operating_hours = WeekHours().add_time_ranges_str(operating_hours)
#         if photo:
#             photo_blob_key = photo[0].key()
#             self.photo = str(photo_blob_key)
#         if pin:
#             self.vendor_code = pin
#         if name:
#             self.name = name
#         if dollar_rating:
#             self.dollar_rating = dollar_rating
#         if category:
#             self.category = category
#         if user_rating:
#             self.user_rating = float(user_rating)
#         if location:
#             self.location = location
#         if neighborhoods:
#             self.neighborhoods = neighborhoods
#         if category_name:
#             self.category_name = category_name
#         if phone_number:
#             self.phone_number = phone_number
#         self.put()



# class ThirdPartyVendorData(db.Model):
#     id_ = db.StringProperty()
#     network = db.StringProperty()
#     name = db.StringProperty(indexed = False)
#     last_updated = db.DateTimeProperty(indexed = False)
#     category = db.StringProperty(indexed = False)
#     location_ = db.GeoPtProperty()
#     city = db.StringProperty()

#     def to_json(self):
#         return {
#             "id" : self.id_,
#             "network" : self.network,
#             "name" : self.name,
#             "lat" : self.location_.lat if self.location_ else None,
#             "lon" : self.location_.lon if self.location_ else None,
#             "city" : self.city
#         }

#     @property
#     def harmonized_vendor(self):
#         return self.parent()

#     @staticmethod
#     def for_id(id_, network):
#         return ThirdPartyVendorData.all().filter('id_',
#                 id_).filter('network', network).get()

#     @staticmethod
#     def for_(vendor, network, id_):
#         return ThirdPartyVendorData.get_by_key_name(network+id_, vendor)

#     @staticmethod
#     def for_network(vendor, network):
#         return ThirdPartyVendorData.all().ancestor(vendor).filter(
#                 'network', network)

#     @staticmethod
#     def for_vendor(vendor):
#         return ThirdPartyVendorData.all().ancestor(vendor)

#     @staticmethod
#     def get_haggle_vendor(id_, network):
#         query = ThirdPartyVendorData.all().filter("id_", id_).filter("network",
#                 network)
#         return query.get().harmonized_vendor if query.count() else None


