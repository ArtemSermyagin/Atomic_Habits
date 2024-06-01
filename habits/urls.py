from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.views import (
    HabitListCreateView,
    HabitRetrieveUpdateDestroyView,
    GetPublicHabitListView
)

app_name = 'habits'
router = DefaultRouter()
urlpatterns = [
    path('habits/', HabitListCreateView.as_view(), name='habit_list_create'),
    path('habits/public/', GetPublicHabitListView.as_view(), name='public_habit_list'),
    path(
        'habits/<int:pk>/',
        HabitRetrieveUpdateDestroyView.as_view(),
        name='habits_retrieve_update_destroy'
    )
]
urlpatterns += router.urls
