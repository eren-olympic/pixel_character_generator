import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PIXEL_SIZE = int(os.getenv("PIXEL_SIZE", 8))
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
    DEFAULT_IMAGE_SIZE = int(os.getenv("DEFAULT_IMAGE_SIZE", 1024))
    
    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required")
        
        if not os.path.exists(cls.OUTPUT_DIR):
            os.makedirs(cls.OUTPUT_DIR)