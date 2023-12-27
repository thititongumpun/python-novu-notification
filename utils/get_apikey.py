from functools import lru_cache
from config import config


@lru_cache
class ApiKey:
    def __init__(self):
        x_api_key = config.settings.x_api_key
        novu_apikey = config.settings.novu_apikey
        supabase_key = config.settings.supabase_key
        supabase_url = config.settings.supabase_url
        self.x_api_key = x_api_key
        self.novu_apikey = novu_apikey
        self.supabase_key = supabase_key
        self.supabase_url = supabase_url
