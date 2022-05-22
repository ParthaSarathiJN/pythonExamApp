from firebase import firebase
import pyrebase

def connection():
    try:
        
        firebaseConfig = {
          'apiKey': "AIzaSyD00-2sgpXCTVoQMUiQakON-FDxPsezJNw",
          'authDomain': "firstapplication-41bdb.firebaseapp.com",
          'databaseURL': "https://firstapplication-41bdb-default-rtdb.firebaseio.com",
          'projectId': "firstapplication-41bdb",
          'storageBucket': "firstapplication-41bdb.appspot.com",
          'messagingSenderId': "830931772497",
          'appId': "1:830931772497:web:9d560a982b0c9dc28d8470",
          'measurementId': "G-MFGLQLD6GX"
        }
        
        
        firebase = pyrebase.initialize_app(firebaseConfig)

        return True,firebase
        
      
    except:

        return False,"null"
            