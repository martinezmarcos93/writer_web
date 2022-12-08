from django.db import models

# Create your models here.
class inicio(models.Model) :
    nombre_pagina = models.CharField(max_length=100)