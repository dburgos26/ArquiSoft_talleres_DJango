from django.db import models
from measurements.models import Measurement

# Create your models here.

class Alarm(models.Model):
    nombre = models.CharField(max_length = 20)
    medidas = models.ManyToManyField(Measurement)

    def __ste__(self):
        return '%s' % (self.nombre)