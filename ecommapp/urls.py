from django.urls import path
from rest_framework import DefaultRouter
from .views import ProductViewSet, OrderViewSet


router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]