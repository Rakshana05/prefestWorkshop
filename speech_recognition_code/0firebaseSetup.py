import pyrebase


config = {
  "apiKey": "AIzaSyClastSM-d8sm0AWajY03OnezmkPVCrO04",
  "authDomain": "fir-topythonsample.firebaseapp.com",
  "projectId": "fir-topythonsample",
  "storageBucket": "fir-topythonsample.appspot.com",
  "databaseURL":"https://fir-topythonsample-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "messagingSenderId": "936536554705",
  "appId": "1:936536554705:web:f4d0b91b36e8174d7e99f0",
  "measurementId": "G-JL324VD9EC"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

user_data = {"Ridhi" :{"Text": "enjoy the rhythm"},
        "Valarmathi":{"Text": "looking to help you"},
        "Selvi":{"Text": "welcome to the world"},
        "Franc":{"Text": "trial is good"}}

stages_data = {"stage1":0,"stage2":0}

database.child("Users").set(user_data)
database.child("Stages").set(stages_data)