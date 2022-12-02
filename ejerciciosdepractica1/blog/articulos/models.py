from turtle import title
from django.db import models
import django.contrib.auth as auth

# Create your models here.

class Articulo(models.Model):
    autor = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    def _str__(self):
        return title