from geopy.geocoders import Nominatim

def get_location(name):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(name)
    if getLoc:
        return getLoc.latitude, getLoc.longitude
    else:
        return None, None