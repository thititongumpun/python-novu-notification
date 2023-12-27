from utils.get_apikey import ApiKey


def test_get_apikey():
    assert isinstance(ApiKey().x_api_key, str)
    assert isinstance(ApiKey().novu_apikey, str)
    assert isinstance(ApiKey().supabase_key, str)
    assert isinstance(ApiKey().supabase_url, str)
    assert ApiKey().x_api_key is not None
    assert ApiKey().novu_apikey is not None
    assert ApiKey().supabase_key is not None
    assert ApiKey().supabase_url is not None
