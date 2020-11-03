from django.db import models

# Create your models here.
class monday_model1(models.Model):
    day=models.CharField(max_length=30)
    firstperiod=models.CharField(max_length=30)
    secondperiod=models.CharField(max_length=30)
    thirdperiod=models.CharField(max_length=30)
    fourthperiod=models.CharField(max_length=30)
    fifthperiod=models.CharField(max_length=30)
    sixthperiod=models.CharField(max_length=30)
    seventhperiod=models.CharField(max_length=30)
    eightperiod=models.CharField(max_length=30)

class column_model1(models.Model):
    periodno=models.IntegerField()
    monday=models.CharField(max_length=30)
    tuesday=models.CharField(max_length=30)
    wednesday=models.CharField(max_length=30)
    thrusday=models.CharField(max_length=30)
    friday=models.CharField(max_length=30)
    saturday=models.CharField(max_length=30)
    