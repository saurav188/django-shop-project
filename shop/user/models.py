from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    profile_picture=models.ImageField(upload_to='media/img',null=True)
    phone_no=models.IntegerField(null=True)
    address=models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.first_name