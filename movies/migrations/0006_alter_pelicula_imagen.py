# Generated by Django 5.1.1 on 2024-10-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]