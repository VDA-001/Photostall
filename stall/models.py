from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    cimage=models.ImageField(upload_to="images")
    def __str__(self):
        return self.title
class Image(models.Model):
    image=models.ImageField(upload_to="images")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
