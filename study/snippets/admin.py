from django.contrib import admin
from django.contrib.admin import ModelAdmin
from snippets.models import Snippet

# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(ModelAdmin):
    pass

