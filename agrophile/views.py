from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
import requests
import numpy as np
import config
import pickle
model_path = 'savedmodels/RandomForest.pkl'
model = pickle.load(
    open(model_path, 'rb'))
def home(request):
    return render(request,'home.html')
def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Taken')
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'email Taken')
                return redirect('login')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print('user created')
        else:
            messages.info(request,'password not matching....')    
            return redirect('login')
        return redirect('/')
    else:    
        return render(request,'login.html')
    
def about(request):
    return render(request,'about.html')
def prediction(request):
    return render(request,'prediction.html')
def contact(request):
    return render(request,'contact.html')
def info(request):
    return render(request,'info.html')    
def weather_fetch(city_name):
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None
def crop_prediction(request):
    #title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.POST['nitrogen'])
        P = int(request.POST['phosphorous'])
        K =int( request.POST['pottasium'])
        ph =float(request.POST['ph'])
        rainfall =float(request.POST['rainfall'])

        
        #state = request.POST["State"]
        
        city = str(request.POST['City'])

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = model.predict(data)
            final_prediction = my_prediction[0]

            return render(request,'result.html', {'prediction':final_prediction})

        else:

            return render(request,'error.html')        
    