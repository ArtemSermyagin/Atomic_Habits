from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializers


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class GetPublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializers
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]


class HabitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
