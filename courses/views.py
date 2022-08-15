from django.shortcuts import render
from courses.models import Chapter, Course
from django.views.generic import ListView, DetailView

class CoursesList(ListView):
    queryset = Course.objects.all()
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10
    
class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        chapters = Chapter.objects.filter(course=course)
        context['chapters'] = chapters
        return context