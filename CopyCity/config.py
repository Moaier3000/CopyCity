import os
class Config:
    DEBUG = True
    GOOGLE_MAPS_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
