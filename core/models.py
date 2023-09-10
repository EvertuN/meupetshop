from django.db import models
from stdimage import StdImageField


# Create your models here.
class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Especie(Base):
    especie = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering = ('especie',)

    def __str__(self):
        return self.especie


class Cliente(Base):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Animal(Base):
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=2)
    sexo = models.CharField(max_length=20)
    foto = StdImageField(upload_to='equipe',
                         variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})
    especie = models.ForeignKey(Especie, models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome
