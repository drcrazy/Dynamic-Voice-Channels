from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = '.env'

    discord_token: str

    bot_client_id: int

    owner_id: int

    command_prefix: str = 'pg'


settings = Settings()
