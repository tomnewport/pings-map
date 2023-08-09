import geoip2
from datetime import date
import pymongo
from .models import Location, Country, Ping
from dotenv import load_dotenv
import os
def get_ip_addr(start_date: date, end_date: date):
    load_dotenv()
    mongo_url = os.environ.get("MONGO_URL")
    client = pymongo.MongoClient(mongo_url)
    with geoip2.database.Reader('c://Users/dcsam/Documents/pings-map/GeoLite2-City.mmdb') as reader:
        for addr in list(client["grouper_pings"]["mux_scan_segment_summary"].find({'logged':{"$gte":start_date, "$lt":end_date}})):
            try:
                response = reader.city(addr["remote_addr"])
                longitude = response.location.longitude
                latitude = response.location.latitude
                country_name = response.country.name
                country_code = response.country.iso_code
                date = addr['logged']
                location = Location(longitude=longitude, latitude=latitude)
                location.save()
                country = Country(country_name=country_name, country_code=country_code)
                country.save()
                ping = Ping(country=country, location=location, time=date, ip_addr=addr)
                ping.save()
            except Exception as AddressNotFoundError:
                continue
