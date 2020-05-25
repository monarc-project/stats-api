import os

HOST = "0.0.0.0"
PORT = os.environ.get("PORT")
DEBUG = False
TESTING = False

ADMIN_EMAIL = "info@cases.lu"
ADMIN_URL = "https://www.cases.lu"

MONGODB_HOST = "localhost"

REMOTE_STATS_SERVER = 'http://127.0.0.1:5000'
