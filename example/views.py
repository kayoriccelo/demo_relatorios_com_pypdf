from core.views import BaseReportView
from .models import Example
from .serializers import ExampleReportSerializer


class ExampleReportViewSet(BaseReportView):
    template = 'report.html'
    queryset = Example.objects.all().distinct()
    serializer_class = ExampleReportSerializer
