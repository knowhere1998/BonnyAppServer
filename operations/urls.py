from django.conf.urls import url, include
from .serializers import router
from django.http import HttpResponse

from .views import index

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'index/', index),
]
