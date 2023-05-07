from rest_framework import serializers
from app.models import ExplorerDeliveredUI, ExplorerOverviewItem

class ExplorerDeliveredUISerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplorerDeliveredUI
        fields = ['id', 'name', 'category', 'itens']
        depth = 1
        
class ExplorerOverviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplorerOverviewItem
        fields = ['id', 'title', 'description']