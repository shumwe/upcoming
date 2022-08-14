from django.contrib import admin
from courses.models import Course, Chapter

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['heading','sub_heading', 'creator', 'created']
    list_filter = ['tags', 'created']
    prepopulated_fields = {'slug': ('heading',)}
    search_fields = ['tags', 'heading', 'sub_heading']