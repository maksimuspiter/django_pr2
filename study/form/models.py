from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    author = models.ForeignKey('Portfolio', on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return f"{self.author}:{self.title}"

    class Meta:
        ordering = ['id']


class Portfolio(models.Model):
    nickname = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
