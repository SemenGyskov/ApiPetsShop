
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import PetViewSet, TypeViewSet, StatViewSet, CategoryViewSet, OrderViewSet

router = routers.SimpleRouter()
router.register(r'pet', PetViewSet)
router.register(r'type', TypeViewSet)
router.register(r'stat', StatViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
