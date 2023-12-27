from supabase import create_client, Client


class Supabase():
    def __init__(self, url, key):
        self.client: Client = create_client(url, key)

    def select(self, table, data):
        return self.client.table(table).select(data).execute()
