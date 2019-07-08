from django.db import models


class Example(models.Model):
    codigo = models.CharField(max_length=6)
    descricao = models.CharField(max_length=80)
    conteudo = models.CharField(max_length=80)
    valor_1 = models.FloatField(default=0)
    valor_2 = models.FloatField(default=0)
    valor_3 = models.FloatField(default=0)
    valor_4 = models.FloatField(default=0)

    class Meta:
        db_table = 'example'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descricao)
