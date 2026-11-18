from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongo_url: str
    mongo_db: str = "secondbrain"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()