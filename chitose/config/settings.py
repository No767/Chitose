from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    NAME: str
    DESCRIPTION: str
    VERSION: str


settings = Settings(NAME="Chitose", DESCRIPTION="The backend API for Akari", VERSION="v0.1.0") 
