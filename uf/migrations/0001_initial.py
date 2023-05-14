# Generated by Django 4.1 on 2023-05-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidaddeFomento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(unique=True, verbose_name='Fecha')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor Diario')),
            ],
            options={
                'verbose_name': 'Unidad de Fomento',
                'verbose_name_plural': 'Unidad de Fomento',
                'ordering': ['fecha'],
            },
        ),
    ]
