from django.contrib import admin
from app.models import Post, User

class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'view_average', 'is_published')
    list_filter = ('title', 'view_average')
    list_per_page = True
    list_display_links = ['title']
    search_fields = ['title']
    
class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_display_links = ['name']
    list_filter = ('name', 'age')
    list_per_page = True
    search_fields = ['name']
       
admin.site.register(Post, Posts)
admin.site.register(User, Users)