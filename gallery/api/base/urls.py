from rest_framework import routers
from django.conf.urls import url
from gallery.api.base.views import GroupViewSet
from gallery.api.base.views import PhotoViewSet
from gallery.api.base import views
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'groups', GroupViewSet, base_name='groups')
router.register(r'photos', PhotoViewSet, base_name='photos')


urlpatterns = router.urls
urlpatterns = urlpatterns + [
    url(r'group/(?P<id>[-@\w]+)/', views.get_photo_id, name='group'),# regular expression for word, char,or symbols:- [-@\w]+
]
