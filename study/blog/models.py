from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    # author = models.ForeignKey('Portfolio', on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return f"{self.author}:{self.title}"


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



# class Portfolio(models.Model):
#     nickname = models.CharField(max_length=255)
#     user = models.OneToOneField(User, on_delete=models.PROTECT, related_query_name='portfolio')
#
#     def __str__(self):
#         return self.nickname
