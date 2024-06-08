from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','category','stock','edition','created_at']
    filter_horizontal = ('author',)
    list_filter = ["category"]