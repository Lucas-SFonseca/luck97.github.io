# Create your models here.
from django.db import models

class Disciplinas(models.Model):

    professor = models.CharField("Professor", max_length=50)
    horasMensais = models.CharField("horasMensais", max_length=100)
    horaAula = models.CharField("horaAula", max_length=10)
    ementa = models.CharField("ementa",max_length=1000)
