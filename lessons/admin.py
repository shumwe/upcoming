from django.contrib import admin
from lessons.models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'posted']
    list_filter = ['posted', 'tags',]
    search_fields = ['title', 'author', 'tags']
    prepopulated_fields = {'slug': ('title',)}