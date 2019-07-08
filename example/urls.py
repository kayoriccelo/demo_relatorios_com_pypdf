from django.conf.urls import url
from .views import ExampleViewSet

urlpatterns = [
    url(r'^example-pdf/', ExampleViewSet.as_view(), name='example-pdf'),
]