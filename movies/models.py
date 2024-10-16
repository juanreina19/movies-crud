# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Actores(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return f'{self.nombre}'


class Alquiler(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_ejemplar = models.ForeignKey('Ejemplar', models.DO_NOTHING, db_column='Id_ejemplar', blank=True, null=True)  # Field name made lowercase.
    fecha_alquiler = models.CharField(db_column='Fecha_Alquiler', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_devolucion = models.CharField(db_column='Fecha_Devolucion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    as_delivered = models.IntegerField(blank=True, null=True)
    id_socio = models.ForeignKey('Socio', models.DO_NOTHING, db_column='Id_socio', blank=True, null=True)  # Field name made lowercase.



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Codeudor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_socio = models.ForeignKey('Socio', models.DO_NOTHING, db_column='Id_socio', blank=True, null=True)  # Field name made lowercase.
    id_codeudor = models.ForeignKey('Socio', models.DO_NOTHING, db_column='Id_Codeudor', related_name='codeudor_id_codeudor_set', blank=True, null=True)  # Field name made lowercase.

    
    def __str__(self):
        return f'{self.id_codeudor}'


class Director(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre.capitalize()



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ejemplar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estado_conservacion = models.CharField(db_column='Estado_conservacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_pelicula = models.ForeignKey('Pelicula', models.DO_NOTHING, db_column='Id_Pelicula', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return  f'{self.id_pelicula}'

class Pelicula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    imagen = models.ImageField(upload_to='img/', blank=False, null=True)
    titulo = models.CharField(db_column='Titulo', max_length=255, blank=False, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=255, blank=False, null=True)  # Field name made lowercase.
    productor = models.CharField(db_column='Productor', max_length=255, blank=False, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', max_length=255, blank=False, null=True)  # Field name made lowercase.
    id_director = models.ForeignKey(Director, models.DO_NOTHING, db_column='ID_Director', blank=False, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.titulo}' 
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    


class Reparto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='Id_Pelicula', blank=False, null=True)  # Field name made lowercase.
    id_actores = models.ForeignKey(Actores, models.DO_NOTHING, db_column='Id_Actores', blank=False, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.id_pelicula} - {self.id_actores}'


class Socio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=255, blank=False, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=False, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=False, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=255, blank=False, null=True)  # Field name made lowercase.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='socio', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'
