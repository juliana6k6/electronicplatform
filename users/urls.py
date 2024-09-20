from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView


app_name = UsersConfig.name


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("user/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
]
