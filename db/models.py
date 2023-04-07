# db/models.py
from django.db import models
from manage import init_django

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    # created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# define models here
class Permanencias(Model):
    sexo = models.TextField(max_length=200)
    pais = models.TextField(max_length=200)
    nacimiento = models.DateField()
    actividad = models.CharField(max_length=200)
    profesion = models.CharField(max_length=200)
    estudios = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    tit_dep = models.CharField(max_length=4)
    autoridad = models.CharField(max_length=400)
    beneficio_agrupado = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    mes = models.CharField(max_length=200)

