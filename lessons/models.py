from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

#user = get_user_model()

class Lesson(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=160, null=True, blank=True)
    featured_image = models.ImageField(upload_to="lesson_image", default="not_available.png")
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=55)
    content = models.TextField()
    tags = TaggableManager()
    publish = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)