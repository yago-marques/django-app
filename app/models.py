from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_average = models.DecimalField(decimal_places=2, max_digits=5)
    is_published = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title