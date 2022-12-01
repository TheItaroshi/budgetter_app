import firebase_admin
from firebase_admin import credentials, db

creds = credentials.Certificate("../confidentials/pjanas_budgetapp_firebase_adminsdk.json")
firebase_admin.initialize_app(creds, {
    'databaseURL': 'https://pjanas-budgetapp-default-rtdb.europe-west1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')

data = ref.get()
print(data.get("Data").get("Stack"))
