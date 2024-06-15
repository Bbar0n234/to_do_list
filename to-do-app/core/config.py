from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1RouterConfig(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiRouterConfig(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
          "ix": "ix_%(column_0_label)s",
          "uq": "uq_%(table_name)s_%(column_0_name)s",
          "ck": "ck_%(table_name)s_%(constraint_name)s",
          "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
          "pk": "pk_%(table_name)s"
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",

        env_prefix="APP_CONFIG__",
        case_sensitive=False,
        env_nested_delimiter='__',

    )
    run: RunConfig = RunConfig()
    api: ApiRouterConfig = ApiRouterConfig()
    api_v1: ApiV1RouterConfig = ApiV1RouterConfig()
    db: DataBaseConfig


settings = Settings()
print(settings.db.url)

