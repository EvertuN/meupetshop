from django.contrib import admin
from core.models import Cliente, Especie, Animal


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('especie', 'ativo')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'bairro', 'cep', 'cidade', 'estado', 'telefone', 'ativo', 'criado')
    list_editable = ('ativo',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'ativo', 'criado')
