from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Store(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    
    def __Str__(self):
        return self.title
    
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254)
    
    def __str__(self) -> str:
        return self.user.username