from core.views import BaseReportView
# from example.filters import ExampleFilter
from .models import Example
from .serializers import ExampleReportSerializer


class ExampleReportViewSet(BaseReportView):
    template = 'base/resumo.html'
    queryset = Example.objects.all().distinct()
    serializer_class = ExampleReportSerializer
    # filter_class = ExampleFilter
