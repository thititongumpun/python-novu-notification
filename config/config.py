from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    novu_apikey: str
    x_api_key: str
    supabase_url: str
    supabase_key: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()