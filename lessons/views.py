from django.shortcuts import render
from lessons.models import Lesson
from django.views.generic import ListView, DetailView


class LessonListView(ListView):
    queryset = Lesson.objects.filter(publish=True).order_by('-posted')
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'
    paginate_by = 10
    
class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.get_object()
        related_lessons = lesson.tags.similar_objects()[:2]
        context['related_lessons'] = related_lessons
        return context