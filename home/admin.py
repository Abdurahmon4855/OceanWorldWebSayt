from django.contrib import admin
from .models import *


admin.site.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'habitat', 'size', 'lifespan')
    list_filter = ('category', 'habitat')
    search_fields = ('name', 'description', 'interesting_fact')
    