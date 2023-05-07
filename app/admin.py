from django.contrib import admin
from app.models import ExplorerDeliveredUI, ExplorerOverviewItem

class ExplorerDeliveredUIs(admin.ModelAdmin):
    list_display = ('id', 'image', 'name')
    list_filter = ['name']
    list_per_page = True
    list_display_links = ['name']
    search_fields = ['name']
    
class ExplorerOverviewItems(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ['title']
    list_filter = ('title', 'description')
    list_per_page = True
    search_fields = ['title']
       
admin.site.register(ExplorerDeliveredUI, ExplorerDeliveredUIs)
admin.site.register(ExplorerOverviewItem, ExplorerOverviewItems)