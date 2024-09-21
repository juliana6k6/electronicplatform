from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = "__all__"


class ListUserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя в списке пользователей"""

    class Meta:
        model = User
        fields = ("id", "email", "phone", "first_name", "last_name")
