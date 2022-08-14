from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

User = get_user_model()

class Lesson(models.Model):
    title = models.CharField(max_length=155)
    slug = models.SlugField(max_length=160, null=True, blank=True)
    featured_image = models.ImageField(upload_to="lesson_image", default="not_available.png")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    tags = TaggableManager()
    publish = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}-{self.author.username}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={
            'author': self.author.username,
            'year': self.posted.strftime("%Y"),
            'month': self.posted.strftime("%m"),
            'slug': self.slug})