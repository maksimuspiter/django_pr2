from django.contrib import admin
from django.contrib.admin import ModelAdmin
from form.models import Post, Portfolio, Tag, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Portfolio)
admin.site.register(Tag)
admin.site.register(Category)


