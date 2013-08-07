import third_party_libs
from google.appengine.ext import db

class Location(db.Model):
    city = db.StringProperty()

def make(location):
    location = location or "Unknown"
    location_info = HARMONIZED_LOCATIONS.get(location.lower(), location)
    return Location.get_or_insert(location_info, city=location_info)

HAGGLE_LOCATIONS = [NewYork, Bengaluru] = ["New York City", "Bengaluru"]

HARMONIZED_LOCATIONS = {
    "ny": NewYork,
    "nyc": NewYork,
    "new york": NewYork,
    "new york city": NewYork,
    "bangalore": Bengaluru,
    "bengaluru": Bengaluru,
    "blr": Bengaluru,
    "blore": Bengaluru
}

