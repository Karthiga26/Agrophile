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
model1 = pickle.load(open('savedmodels/classifier.pkl','rb'))
ferti = pickle.load(open('savedmodels/fertilizer.pkl','rb'))
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'* Invalid credentials,Try Again!!!')  
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:        
            return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'* Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'* Email already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email,first_name = first_name, last_name = last_name)
                user.save()
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request,'* Passwords dont match')
            return redirect('signup')  
    else:    
        return render(request,'signup.html')
  
def about(request):
    return render(request,'about.html')
def prediction(request):
    return render(request,'prediction.html')
def fertilizer(request):
    return render(request,'fertilizer.html')
def contact(request):
    return render(request,'contact.html')
def info(request):
    return render(request,'info.html')  
def logout(request):
    auth.logout(request)
    return redirect('/') 
def chickpea(request):
    return render(request,'chickpea.html')
def kidneybeans(request):
    return render(request,'kidneybeans.html') 
def pigeonpeas(request):
    return render(request,'pigeonpeas.html')  
def mothbeans(request):
    return render(request,'mothbeans.html') 
def grapes(request):
    return render(request,'grapes.html') 
def mango(request):
    return render(request,'mango.html') 
def muskmelon(request):
    return render(request,'muskmelon.html') 
def pomegranate(request):
    return render(request,'pomegranate.html')  
def rice(request):
    return render(request,'rice.html')   
def maize(request):
    return render(request,'maize.html')  
def cotton(request):
    return render(request,'cotton.html')  
def jute(request):
    return render(request,'jute.html')  
def blackgram(request):
    return render(request,'blackgram.html') 
def lentil(request):
    return render(request,'lentil.html') 
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
def fertilizer_predict(request):
   
   if request.method=='POST':
     City = str(request.POST.get('City',None))
     mois = int(request.POST['mois'])
     soil = str(request.POST['soil'])
     crop = str(request.POST['crop'])
     nitro = int(request.POST['nitro'])
     pota = int(request.POST['pota'])
     phosp = int(request.POST['phos'])
     if weather_fetch(City) != None:
            temperature, humidity = weather_fetch(City)
            fert_input = np.array([[temperature,humidity,mois,soil,crop,nitro,pota,phosp]])
            fert_predict= ferti.classes_[model1.predict(fert_input)]
            
            return render(request,'fertilizer-result.html',{'recommendation':fert_predict})