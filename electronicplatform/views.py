from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from electronicplatform.models import PlatformUnit, Product
from electronicplatform.permissions import IsActiveUser
from electronicplatform.serializers import ProductSerializer, PlatformUnitSerializer


class PlatformUnitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания звена торговой сети"""
    serializer_class = PlatformUnitSerializer
    permission_classes = [IsActiveUser]


class PlatformUnitListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка уже существующих звеньев"""
    serializer_class = PlatformUnitSerializer
    queryset = PlatformUnit.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class PlatformUnitDetailAPIView(generics.RetrieveAPIView):
    """Контроллер просмотра звена торговой сети"""
    serializer_class = PlatformUnitSerializer
    queryset = PlatformUnit.objects.all()
    permission_classes = [IsActiveUser]


class PlatformUnitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для редактирования звена торговой сети"""
    serializer_class = PlatformUnitSerializer
    queryset = PlatformUnit.objects.all()
    permission_classes = [IsActiveUser]


class PlatformUnitDeleteAPIView(generics.DestroyAPIView):
    """Контроллер для удаления звена торговой сети"""
    queryset = PlatformUnit.objects.all()
    permission_classes = [IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]

