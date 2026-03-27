import os
import dotenv

dotenv.load_dotenv()

class Config:
    DEBUG = True
    GOOGLE_MAPS_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
    SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY")
