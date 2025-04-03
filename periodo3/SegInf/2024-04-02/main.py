import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAqnq7jWL0--KVZnr5emFz1JQWieO5urFE",
  "authDomain": "bsi-seginf.firebaseapp.com",
  "projectId": "bsi-seginf",
  "storageBucket": "bsi-seginf.firebasestorage.app",
  "messagingSenderId": "392766567382",
  "appId": "1:392766567382:web:1a45c59d3e20f101136a77",
  "databaseURL": "",
}

APP = pyrebase.initialize_app(firebaseConfig)