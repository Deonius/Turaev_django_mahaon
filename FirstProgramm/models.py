from django.db import models
from django.utils import timezone
class MyArticle(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null = True)
# Create your models here.
