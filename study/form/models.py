from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


# class PortfolioManager(models.Manager):
#     def order_by_post_count(self):
#         return super().get_queryset().annotate(cnt=models.Count('post')).order_by("-cnt")

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    author = models.ForeignKey('Portfolio', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
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
    # objects = models.Manager()
    # new_objects = PortfolioManager()

    def __str__(self):
        return self.nickname


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type',
                                       fk_field='object_id')
