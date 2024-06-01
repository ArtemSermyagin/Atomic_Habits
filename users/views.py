from rest_framework import generics, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(email=serializer.data["email"])
        user.set_password(serializer.data.get("password"))
        user.is_active = True
        user.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

