from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    PROJECT_NAME: str
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl


settings = Settings()
