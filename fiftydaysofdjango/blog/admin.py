from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status", "sponsor"]
    list_filter = ['status', 'created', 'publish', 'author', "sponsor"]
    search_fields = ['title', 'body']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug' : ('title', )}
    raw_id_fields = ['author']
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS