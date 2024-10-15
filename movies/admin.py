from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Alquiler)
admin.site.register(Actores)
admin.site.register(Reparto)
# admin.site.register(Socio)
# admin.site.register(Codeudor)
# admin.site.register(Ejemplar)


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    readonly_fields = ('id',)
    exclude = ('user',) 

@admin.register(Codeudor)
class CodeudorAdmin(admin.ModelAdmin):
    list_display = ('id_socio', 'id_codeudor')

@admin.register(Ejemplar)
class EjemplarAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado_conservacion', 'id_pelicula')
    readonly_fields = ('id',)
