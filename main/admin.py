from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ("id", "title")
	search_fields = ("title",)
	prepopulated_fields = {'slug':('title',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "genre")
	search_fields = ("title", "description")
	list_filter = ("genre", "created_at")
	prepopulated_fields = {'slug':('title',)}
