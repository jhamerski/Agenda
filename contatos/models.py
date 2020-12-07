from django.db import models
from django.utils import timezone


# class categoria sendo criada
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    # mostra string referente ao nome
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)  # opcional
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    # ao deletar uma categoria nada acontece com seus vinculos
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')

    # mostra string referente ao nome
    def __str__(self):
        return self.nome
