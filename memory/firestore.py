import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from memory.config import config

# using an API key for a service account. not recommended for production
# TODO is there a way to use the emulator without providing real creds?
cred = credentials.Certificate(config['GOOGLE_APPLICATION_CREDENTIALS'])

if config["ENV"] == "prod":
    app = firebase_admin.initialize_app(cred)

elif config["ENV"] in ("test", "dev"):
    app = firebase_admin.initialize_app(
        cred,
        options={
        'projectId': config["FIRESTORE_PROJECT_ID"],
        'databaseURL': config["FIRESTORE_EMULATOR_HOST"],
    })

db = firestore.client()
