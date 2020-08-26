from django.db import models

# Create your models here.
from django.urls import reverse


class ESPdata(models.Model):
    temperatura = models.IntegerField(default=0)
    umidita= models.IntegerField(default=0)
    pressione = models.IntegerField(default=0)	
    pioggia = models.IntegerField(default=0)
    posizione = models.CharField(max_length=30)
     #data= models.DateTimeField('date published')	

    # on submit click on the product entry page, it redirects to the url below. 
    def get_absolute_url(self):
        return reverse('modelformsESPtesi:index')