from django.db import models

class ExplorerOverviewItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
class ExplorerDeliveredUI(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    itens = models.ManyToManyField(ExplorerOverviewItem, blank=False)
    
    def __str__(self) -> str:
        return self.title
