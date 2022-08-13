from django.shortcuts import render
from lessons.models import Lesson
from django.views.generic import ListView, DetailView


class LessonListView(ListView):
    queryset = Lesson.objects.all()
    teplate_name = 'lessons/lessons_index.html'
    context_object_name = 'lessons'
    paginate_by = 2 #20