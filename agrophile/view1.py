from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
import requests
import numpy as np
import config
import pickle
model_path = 'savedmodels/RandomForest.pkl'
model = pickle.load(
    open(model_path, 'rb'))
#model=load('./savedmodels/RF.joblib')
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def prediction(request):
   # title = 'Harvestify - Crop Recommendation'
    return render(request,'prediction.html')
def contact(request):
    return render(request,'contact.html')



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

            return render(request,'crop-result.html', {'prediction':final_prediction})

        else:

            return render(request,'try_again.html')