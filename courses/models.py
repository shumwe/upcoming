from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    heading = models.CharField(max_length=155)
    sub_heading = models.CharField(max_length=155, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField()
    tags = TaggableManager()
    lesson_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)