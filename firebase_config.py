import firebase_admin
from firebase_admin import credentials, firestore, auth

# Path to your service account key JSON file
cred = credentials.Certificate("C:/Users/Shiro/Downloads/CodeCraft/backend/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()