from django.db import models


class Example(models.Model):
    code = models.CharField(max_length=6)
    description = models.CharField(max_length=80)
    content = models.CharField(max_length=80)
    value_1 = models.FloatField(default=0)
    value_2 = models.FloatField(default=0)
    value_3 = models.FloatField(default=0)
    value_4 = models.FloatField(default=0)

    class Meta:
        db_table = 'example'

    def __str__(self):
        return '%s - %s' % (self.code, self.description)
