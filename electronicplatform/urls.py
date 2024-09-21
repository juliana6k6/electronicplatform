from django.urls import path
from rest_framework.routers import DefaultRouter

from electronicplatform.apps import ElectronicplatformConfig
from electronicplatform.views import (
    PlatformUnitCreateAPIView,
    PlatformUnitDeleteAPIView,
    PlatformUnitDetailAPIView,
    PlatformUnitListAPIView,
    PlatformUnitUpdateAPIView,
    ProductViewSet,
)

app_name = ElectronicplatformConfig.name
router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")


urlpatterns = [
    path(
        "platformunitlist/", PlatformUnitListAPIView.as_view(), name="platformunitlist"
    ),
    path(
        "platformunit/<int:pk>/",
        PlatformUnitDetailAPIView.as_view(),
        name="platformunit-detail",
    ),
    path(
        "platformunit/create/",
        PlatformUnitCreateAPIView.as_view(),
        name="platformunit-create",
    ),
    path(
        "platformunit/<int:pk>/update/",
        PlatformUnitUpdateAPIView.as_view(),
        name="platformunit-update",
    ),
    path(
        "platformunit/<int:pk>/delete/",
        PlatformUnitDeleteAPIView.as_view(),
        name="platformunit-delete",
    ),
] + router.urls
