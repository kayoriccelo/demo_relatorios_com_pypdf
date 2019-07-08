from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    url(r'^reports/', include('example.urls')),
]
