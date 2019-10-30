from django.db import models
from django.utils import timezone

# Create your models here.
class EntryItem(models.Model):
    unique_id = models.CharField(primary_key = True, max_length=100)
    task_id = models.CharField(max_length=100)
    keyword = models.CharField(max_length=40)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.keyword

    class Meta:
        ordering = ["-date"]

class ArticleItem(models.Model):
    entry = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    headline = models.CharField(max_length=100)
    content = models.TextField()
 
    def __str__(self):
        return self.headline

