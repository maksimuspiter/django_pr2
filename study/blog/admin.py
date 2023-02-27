from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import Post, Portfolio

# Register your models here.
@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    pass
