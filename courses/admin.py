from django.contrib import admin
from courses.models import Course, Chapter

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['heading','sub_heading', 'creator', 'created']
    list_filter = ['created','creator']
    prepopulated_fields = {'slug': ('heading',)}
    search_fields = ['tags', 'heading', 'sub_heading']
    
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['course','chapter_number_in_course','title','created']
    list_filter = ['created','updated',]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['tags', 'title', 'course']