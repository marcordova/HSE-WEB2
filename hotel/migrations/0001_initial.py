# Generated by Django 3.1.3 on 2021-01-18 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de habitación')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Número de habitación')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, upload_to='hotel', verbose_name='Imagen')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.type')),
            ],
            options={
                'verbose_name': 'Habitación',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['created_on'],
            },
        ),
    ]
