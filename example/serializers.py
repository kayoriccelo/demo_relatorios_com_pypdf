from collections import OrderedDict
from rest_framework import serializers


class ExampleReportSerializer(serializers.Serializer):
    def to_representation(self, instance):

        example_dict = OrderedDict()
        example_dict['code'] = instance.code
        example_dict['description'] = instance.description
        example_dict['content'] = instance.content
        example_dict['value_1'] = instance.value_1
        example_dict['value_2'] = instance.value_2
        example_dict['value_3'] = instance.value_3
        example_dict['value_4'] = instance.value_4

        return example_dict
