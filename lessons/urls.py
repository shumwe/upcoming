from django.urls import path
from lessons import views

urlpatterns = [
    path('', views.LessonListView.as_view(), name='lessons_list'),
]