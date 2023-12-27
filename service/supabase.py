from supabase import create_client, Client

from utils.get_apikey import ApiKey


class Supabase():
    def __init__(self):
        url = ApiKey().supabase_url
        key = ApiKey().supabase_key
        self.client: Client = create_client(url, key)

    def select(self, table, data):
        return self.client.table(table).select(data).execute()
