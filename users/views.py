from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer, ListUserSerializer


# class UserCreateView(generics.CreateAPIView):
#     """Регистрация нового пользователя
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         """Переопределение метода для сохранения хешированного пароля в бд (если пароль не хешируется -
#         пользователь не считается активным и токен авторизации не создается)"""
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#
#         password = serializer.data["password"]
#         user = User.objects.get(pk=serializer.data["id"])
#         user.set_password(password)
#         user.is_active = True
#         user.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class UserListAPIView(generics.ListAPIView):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)  # сделали пользователя активным
        user.set_password(user.password)  # хешируется пароль
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
