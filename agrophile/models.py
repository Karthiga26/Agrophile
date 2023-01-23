from django.db import models

# Create your models here.
class Crops(models.Model):
    cropname = models.CharField(max_length=100)
    cropimg =  models.ImageField(upload_to='exercise_pics')
    cropdetails = models.TextField()
    
