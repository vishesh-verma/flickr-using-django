from rest_framework import routers
from django.conf.urls import url
from external_data_sources.api.base import views

router = routers.SimpleRouter(trailing_slash=False)
urlpatterns = [
    url(r'^load_data$', views.load_data, name='load_data'),
]
