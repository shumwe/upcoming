from django.urls import path
from lessons import views

urlpatterns = [
    path('', views.LessonListView.as_view(), name='lessons_list'),
    path('<slug:year>/<slug:month>/<slug:author>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),
]