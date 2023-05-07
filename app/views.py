from rest_framework import viewsets
from rest_framework.response import Response
from app.models import ExplorerDeliveredUI, ExplorerOverviewItem
from app.serializer import ExplorerDeliveredUISerializer, ExplorerOverviewItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ExplorerDeliveredUIViewSet(viewsets.ModelViewSet):
    serializer_class = ExplorerDeliveredUISerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExplorerDeliveredUI.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data

        new_ui = ExplorerDeliveredUI.objects.create(name=data['name'], category=data["category"])

        new_ui.save()

        for item in data["itens"]:
            new_obj = ExplorerOverviewItem.objects.create(title=item["title"], description=item["description"])

            new_obj.save()
            
            overview_obj = ExplorerOverviewItem.objects.get(title=item["title"], description=item["description"])
            new_ui.itens.add(overview_obj)

        serializer = ExplorerDeliveredUISerializer(new_ui)

        return Response(serializer.data)
    
class ExplorerOverviewItemViewSet(viewsets.ModelViewSet):
    serializer_class = ExplorerOverviewItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = ExplorerOverviewItem.objects.all()
        return queryset
