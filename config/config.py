import os
import shutil
from dotenv import load_dotenv

# Check if .env file exists, if not, copy from .env.example
if not os.path.exists('.env'):
    shutil.copy('.env.example', '.env')

# Load environment variables from .env file
load_dotenv()

class Configs:
    def __init__(self):
        self.APP_NAME = os.getenv("APP_NAME")
        self.APP_VERSION = os.getenv("APP_VERSION")