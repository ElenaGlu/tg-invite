import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

CHAT_ID = os.getenv('CHAT_ID')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
