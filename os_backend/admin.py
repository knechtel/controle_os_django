from django.contrib import admin
from . import models
# Register your models here.
from .models import Equipment


class EquipmentInstanceInline(admin.TabularInline):
    model = Equipment


# inlines = [NotesInstanceInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('marca',)


admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Client, ClientAdmin)


# Register your models here.
