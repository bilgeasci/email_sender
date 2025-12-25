# config/settings.py

import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS için standart port
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")