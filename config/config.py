from pydantic_settings import BaseSettings, SettingsConfigDict
from novu.api import EventApi


class Settings(BaseSettings):
    novu_apikey: str
    x_api_key: str

    model_config = SettingsConfigDict(env_file=".env")
