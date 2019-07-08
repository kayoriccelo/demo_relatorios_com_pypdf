from django.conf.urls import url
from .views import ExampleReportViewSet

urlpatterns = [
    url(r'^example-pdf/', ExampleReportViewSet.as_view(), name='example-pdf'),
]