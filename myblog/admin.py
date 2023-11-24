from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['-id']
    search_fields = ['name']

admin.site.register(Category)
admin.site.register(Product)

