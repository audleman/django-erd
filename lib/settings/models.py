from django.db import models

class Setting(models.Model):    
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=1000)

    def __unicode__(self):
        return u'%s:%s' % (self.name, self.value)