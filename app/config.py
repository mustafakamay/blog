from decouple import config

class Settings:
    MONGODB_URL = config('MONGODB_URL', default='')
    MONGODB_NAME = config('MONGODB_NAME', default='myblogdb')
    DEBUG = config('DEBUG', default=False, cast=bool)
    SECRET_KEY = config('SECRET_KEY', default='')

settings = Settings()
