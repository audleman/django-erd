from django.db import models


class ModelRenderSettings(models.Model):

    name = models.CharField(max_length=100)
    fields = models.CharField(max_length=2000, blank=True)
    foreign_keys = models.CharField(max_length=2000, blank=True)
    selected = models.BooleanField(default=False)
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    z = models.IntegerField(default=2)

    def __unicode__(self):
        return '%s [%s, %s, %s, %s]' % (self.name,
                self.top, self.left, self.z, self.selected)
