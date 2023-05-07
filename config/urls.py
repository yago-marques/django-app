from django.contrib import admin
from django.urls import path, include
from app.views import ExplorerDeliveredUIViewSet, ExplorerOverviewItemViewSet
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('deliveredUi', ExplorerDeliveredUIViewSet, basename="deliveredUI")
router.register('overviewItem', ExplorerOverviewItemViewSet, basename="overviewItem")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title='Django Application',
        description='A simple Django REST API',
        version='1.0.0',
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
