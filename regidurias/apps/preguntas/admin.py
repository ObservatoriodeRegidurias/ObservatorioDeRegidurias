from django.contrib import admin
from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')

    search_fields = ('title',)
    # this create the slug field from the title field
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)


# Register your models here.
