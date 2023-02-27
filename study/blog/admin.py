from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import Post, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass
