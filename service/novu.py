from novu.api import EventApi
from utils.get_apikey import ApiKey


class Novu:
    def __init__(self):
        api_key = ApiKey().novu_apikey
        self.event_api = EventApi("https://api.novu.co", api_key)

    def trigger(self, name, recipients, payload):
        return self.event_api.trigger(name, recipients, payload)
