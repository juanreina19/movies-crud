# Generated by Django 5.1.1 on 2024-10-16 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_actores_options_alter_alquiler_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparto',
            name='tipo',
        ),
        migrations.AddField(
            model_name='alquiler',
            name='id_ejemplar',
            field=models.ForeignKey(blank=True, db_column='Id_ejemplar', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.ejemplar'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='id_socio',
            field=models.ForeignKey(blank=True, db_column='Id_socio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.socio'),
        ),
        migrations.AddField(
            model_name='codeudor',
            name='id_codeudor',
            field=models.ForeignKey(blank=True, db_column='Id_Codeudor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='codeudor_id_codeudor_set', to='movies.socio'),
        ),
        migrations.AddField(
            model_name='codeudor',
            name='id_socio',
            field=models.ForeignKey(blank=True, db_column='Id_socio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.socio'),
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='id_pelicula',
            field=models.ForeignKey(blank=True, db_column='Id_Pelicula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.pelicula'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='id_director',
            field=models.ForeignKey(db_column='ID_Director', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.director'),
        ),
        migrations.AddField(
            model_name='reparto',
            name='id_actores',
            field=models.ForeignKey(db_column='Id_Actores', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.actores'),
        ),
        migrations.AddField(
            model_name='reparto',
            name='id_pelicula',
            field=models.ForeignKey(db_column='Id_Pelicula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.pelicula'),
        ),
        migrations.AlterField(
            model_name='actores',
            name='id',
            field=models.BigAutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='codeudor',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='director',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reparto',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='actores',
            table=None,
        ),
        migrations.AlterModelTable(
            name='alquiler',
            table=None,
        ),
        migrations.AlterModelTable(
            name='codeudor',
            table=None,
        ),
        migrations.AlterModelTable(
            name='director',
            table=None,
        ),
        migrations.AlterModelTable(
            name='ejemplar',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pelicula',
            table=None,
        ),
        migrations.AlterModelTable(
            name='reparto',
            table=None,
        ),
        migrations.AlterModelTable(
            name='socio',
            table=None,
        ),
    ]
