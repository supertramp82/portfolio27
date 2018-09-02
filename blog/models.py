from django.db import models
from django.utils import timezone


class Blog(models.Model):
    #dt = timezone.now

    title = models.CharField(max_length=255, default='')
    pub_date = models.DateTimeField()
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/', null=True)
