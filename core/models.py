from django.db import models

# Create your models here.
class MailingList(models.Model):
    subscriber_name = models.CharField(max_length=65, verbose_name="Name ")
    subscriber_email = models.EmailField(verbose_name="Email")
    joined = models.DateTimeField(auto_now=True)
    stop = models.BooleanField(default=False, help_text="stop receiving our emails")
    
    def __str__(self):
        return f"{self.subscriber_name}"