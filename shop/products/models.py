from django.db import models

# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=80,unique=True)
    image=models.ImageField(upload_to='media/img')
    price=models.IntegerField()
    produuct_description=models.TextField()

    def __str__(self):
        return self.product_name
