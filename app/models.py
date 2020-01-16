from django.db import models

class data(models.Model):
    user=models.CharField(max_length=30)
    time=models.DateField(auto_now_add=True)
    inputfile_path=models.CharField(max_length=50)
    processedfile_path=models.CharField(max_length=50,blank=True)
    prediction=models.CharField(max_length=30,blank=True)
class launchpad(models.Model):
    user=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    latitude=models.FloatField()
    longitude=models.FloatField()
    altitude=models.FloatField(default=0, null=True)
