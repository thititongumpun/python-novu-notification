from supabase import create_client, Client


class Supabase():
    def __init__(self, url, key):
        self.supabase: Client = create_client(url, key)

    def select(self, table, data):
        return self.supabase.table(table).select(data).execute()
