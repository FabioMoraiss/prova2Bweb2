from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.models.CharField( max_length=50)
    email = models.models.CharField( max_length=50)
    telefone = models.models.CharField( max_length=50)
    senha = models.models.CharField( max_length=50)
    def __str__(self):
        return self.nome