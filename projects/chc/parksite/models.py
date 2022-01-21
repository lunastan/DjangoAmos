from django.db import models

class FaceImage(models.Model) :
    faceId = models.AutoField(primary_key=True)
    faceImg = models.ImageField(upload_to='images/')

# Create your models here.
