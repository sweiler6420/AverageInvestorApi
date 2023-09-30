from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    sm_secret_key: str
    sm_region: str

    class Config:
        env_file = ('avg_inv_api\.env')

settings = Settings()