from django.contrib import admin
from Blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter= ('status','author','created')
    search_fields=('title','body')
    raw_id_fields = ('author',)
    prepopulated_fields ={'slug':('title',)}
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(Post,PostAdmin)