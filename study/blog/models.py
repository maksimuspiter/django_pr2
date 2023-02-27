from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('Portfolio', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.author.nickname}:{self.title}"


class Portfolio(models.Model):
    nickname = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nickname
