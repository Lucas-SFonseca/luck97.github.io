# Create your models here.
from django.db import models

class Disciplinas(models.Model):

    nome = models.CharField("nome",max_length=240)
    carga_horaria = models.IntegerField("carga_horaria")
    teoria = models.DecimalField("teoria",max_digits=10,decimal_places=3)
    pratica = models.DecimalField("teoria",max_digits=10,decimal_places=3)
    ementa = models.TextField("ementa")
    competencias = models.TextField("competencias")
    habilidades = models.TextField("habilidades")
    conteudo = models.TextField("conteudo")
    bibliografia_basica = models.TextField("bibliografia_basica")
    bibliografia_complementar = models.TextField("bibliografia_complementar")
