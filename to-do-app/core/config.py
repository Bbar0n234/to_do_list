from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiRouterConfig(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",

        env_prefix="APP_CONFIG__",
        case_sensitive=False,
        env_nested_delimiter='__',

    )
    run: RunConfig = RunConfig()
    api: ApiRouterConfig = ApiRouterConfig()
    db: DataBaseConfig


settings = Settings()
print(settings.db.url)

