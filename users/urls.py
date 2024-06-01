from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path(
        'users/<int:pk>/',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='users_retrieve_update_destroy'
    ),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
