from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.urls import reverse
import readtime

User = get_user_model()

class Course(models.Model):
    heading = models.CharField(max_length=155)
    sub_heading = models.CharField(max_length=155)
    featured_image = models.ImageField(upload_to='courses', default='courses/course_default.png')
    slug = models.SlugField(unique=True, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.heading)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'username':self.creator.username,
                                                'year':self.created.strftime("%Y"),
                                                'month':self.created.strftime("%m"),
                                                'slug':self.slug})
    
    def __str__(self):
        return f"{self.heading}"
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    tags = TaggableManager()
    chapter_number_in_course = models.IntegerField(default=1, help_text='use integers')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    @property
    def get_readtime(self):
        res = readtime.of_html(self.content)
        return res
    
    def get_absolute_url(self):
        return reverse('chapter_detail', kwargs={'course': self.course.slug,
                                                 'username': self.author.username,
                                                 'year': self.created.strftime("%Y"),
                                                 'month':self.created.strftime("%m"),
                                                 'slug':self.slug,
                                                 })