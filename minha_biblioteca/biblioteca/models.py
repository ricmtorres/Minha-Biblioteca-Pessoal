from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=155)
    senha = models.CharField(max_length=122)


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=155)
    ano_publicacao = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)



