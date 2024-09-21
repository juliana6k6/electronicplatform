from rest_framework import serializers

from electronicplatform.models import PlatformUnit, Product


class PlatformUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformUnit
        fields = "__all__"


class PlatformUnitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformUnit
        exclude = ["debt_supplier"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
