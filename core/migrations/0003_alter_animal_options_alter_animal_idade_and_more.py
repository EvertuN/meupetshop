# Generated by Django 4.2.5 on 2023-09-09 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_animal_cliente_especie_remove_funcionario_cargo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='idade',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(max_length=20),
        ),
    ]
