"""karthi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('agrophile.urls')),
    path('login/',include('agrophile.urls')),
    path('logout/',include('agrophile.urls')),
    path('signup/',include('agrophile.urls')),
    path('about/',include('agrophile.urls')),
    path('prediction/',include('agrophile.urls')),
    path('fertilizer/',include('agrophile.urls')),
    path('contact/',include('agrophile.urls')),
    path('info/',include('agrophile.urls')),
    path('chickpea/',include('agrophile.urls')),
    path('kidneybeans/',include('agrophile.urls')),
    path('mothbeans/',include('agrophile.urls')),
    path('pigeonpeas/',include('agrophile.urls')),
    path('grapes/',include('agrophile.urls')),
    path('mango/',include('agrophile.urls')),
    path('muskmelon/',include('agrophile.urls')),
    path('pomegranate/',include('agrophile.urls')),
    path('rice/',include('agrophile.urls')),
    path('maize/',include('agrophile.urls')),
    path('cotton/',include('agrophile.urls')),
    path('jute/',include('agrophile.urls')),
    path('blackgram/',include('agrophile.urls')),
    path('lentil/',include('agrophile.urls')),
    path('admin/', admin.site.urls),    
]
