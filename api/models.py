import email
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CreateUsers(models.Model):
    username = models.CharField(max_length=10 )
    email = models.EmailField(max_length=50)
    password = models.TextField()
    update_at = models.DateTimeField(auto_now= True)
    
class Users(AbstractUser):
    user = models.ForeignKey(CreateUsers, on_delete=models.CASCADE, null=True)

