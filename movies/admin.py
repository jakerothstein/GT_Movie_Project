from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
admin.site.register(Movie,MovieAdmin)

