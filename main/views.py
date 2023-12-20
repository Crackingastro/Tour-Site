from django.shortcuts import render
import pyrebase

from django.shortcuts import redirect
# Create your views here.

# hello is my main edit and here it is
firebaseConfig = {
  "apiKey": "AIzaSyBCBDQQouIknZD8dg6rx8vVfe5OwBKPJFM",
  "authDomain": "tour-page-4a701.firebaseapp.com",
  "projectId": "tour-page-4a701",
  "databaseURL": "https://tour-page-4a701-default-rtdb.firebaseio.com",
  "storageBucket": "tour-page-4a701.appspot.com",
  "messagingSenderId": "319393656479",
  "appId": "1:319393656479:web:7831a5796ce7f8eb44bcaa",
  "measurementId": "G-7HQFF5FWS5",
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()

# Render Home Page
def home(response):
    return render(response, "main/tour.html", {})

# Render Login Page
def login(response):
    if response.method == "POST":  
        email = response.post.get("email") 
        password = response.post.get("password")

        try:
            auth.sign_in_with_email_and_password(email,password)
            return redirect(signsuccess)
            
        except:
            return render(response, "main/Login.html", {"error":"error"})

    return render(response, "main/Login.html", {})

# Render password reset Page
def Passwordreset(response):
    if response.method == "POST":  
        email = response.post.get("email") 
        try:
            auth.send_password_reset_email(email)
        except:
            return render(response, "main/Passwordreset.html", {"error":"error"})
    return render(response, "main/Passwordreset.html", {})

# Render Signup Page
def signup(response):
    if response.method == "POST":

        first_name = response.POST.get("first-name")
        last_name = response.POST.get("last-name")
        user_name = response.POST.get("user-name")
        country = response.POST.get("country")
        email = response.POST.get("email")
        password = response.POST.get("password")
        confirm = response.POST.get("confirm")


        if password != confirm:
            arr = [first_name,last_name,user_name,country,email]
            return render(response, "main/sign.html", {'error':arr,'cat':'bat'})
        
        try:  
            #authutication happens here      
            user = auth.create_user_with_email_and_password(email,password)
            
            
        except:
            return render(response, "main/sign.html", {"error":"error"})
                
        data = {
            "first-name": first_name,
            "last-name": last_name,
            "user-name": user_name,
            "country":country,
        }

        results = db.child("users").push(data, user['idToken'])
        return redirect(signsuccess) 
    return render(response, "main/sign.html", {})

# Render Signsucess Page
def signsuccess(response):
    return render(response, "main/signsuc.html", {})

