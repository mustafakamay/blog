from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.config import settings

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db: AsyncIOMotorDatabase = self.client[settings.MONGODB_NAME]

db = Database()
