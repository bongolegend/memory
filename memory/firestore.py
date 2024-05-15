import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from memory.config import config

# using an API key for a service account. not recommended for production
cred = credentials.Certificate(config['GCP_SERVICE_ACCOUNT_JSON_PATH'])

app = firebase_admin.initialize_app(cred)

db = firestore.client()
