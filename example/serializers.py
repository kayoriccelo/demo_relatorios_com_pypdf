from collections import OrderedDict
from rest_framework import serializers


class ExampleReportSerializer(serializers.Serializer):
    def to_representation(self, instance):

        departamento_dict = OrderedDict()
        departamento_dict['codigo'] = instance.codigo
        departamento_dict['descricao'] = instance.descricao
        departamento_dict['conteudo'] = instance.conteudo
        departamento_dict['valor_1'] = instance.valor_1
        departamento_dict['valor_2'] = instance.valor_2
        departamento_dict['valor_3'] = instance.valor_3
        departamento_dict['valor_4'] = instance.valor_4

        return departamento_dict
