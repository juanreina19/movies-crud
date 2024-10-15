# Generated by Django 5.1.1 on 2024-10-06 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_pelicula_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='id_director',
            field=models.ForeignKey(db_column='ID_Director', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.director'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
