from django.shortcuts import render
from django.db import models
from django_erd.models import ModelRenderSettings


def erd(request):
    # ModelRenderSettings.objects.all().delete()
    for model in models.get_models():
        m, created = ModelRenderSettings.objects.get_or_create(
                name=model._meta.object_name)
        m.fields = ",".join([f.name for f in model._meta.fields])
        foreign_keys = []
        for field in model._meta.fields:
            if field.__class__.__name__ == 'ForeignKey':
                related_table = field.related.parent_model._meta.object_name
                foreign_keys.append("%s:%s" % (field.name, related_table))
        m.foreign_keys = ",".join(foreign_keys)
        m.save()
    return render(request, 'django_erd/erd.html', {
        'title': 'ERD Diagram'})
