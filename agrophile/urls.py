from django.urls import path
from.import views
app_name="my_app"
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('prediction/',views.prediction,name='prediction'),
    path('contact/',views.contact,name='contact'),
    path('crop_prediction/',views.crop_prediction,name='crop_prediction'),
    path('fertilizer/',views.fertilizer,name='fertilizer'),
    path('fertilizer_predict/',views.fertilizer_predict,name='fertilizer_predict'),
    path('info/',views.info,name='info')
]
