from functools import lru_cache
from config import config


@lru_cache
def get_settings():
    return config.Settings()


@lru_cache
class ApiKey:
    def __init__(self):
        settings = get_settings()
        x_api_key = settings.x_api_key
        novu_apikey = settings.novu_apikey
        supabase_key = settings.supabase_key
        supabase_url = settings.supabase_url
        self.x_api_key = x_api_key
        self.novu_apikey = novu_apikey
        self.supabase_key = supabase_key
        self.supabase_url = supabase_url
