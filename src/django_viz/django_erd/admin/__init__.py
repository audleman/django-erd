from django.contrib import admin

from django_erd.models import ModelRenderSettings


class ModelRenderSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fields', 'foreign_keys', 'top', 'left', 'z', 'selected')


admin.site.register(ModelRenderSettings, ModelRenderSettingsAdmin)
