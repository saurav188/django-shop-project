from django.db import models
from user.models import User
# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=80,unique=True)
    image=models.ImageField(upload_to='media/img')
    price=models.IntegerField()
    produuct_description=models.TextField()

    def __str__(self):
        return self.product_name

class order(models.Model):
    delivery_choices=(
        ('Liked','Liked'),
        ('In Cart','In Cart'),
        ('Pending','Pending'),
        ('Left for Delivery','Left for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,choices=delivery_choices,default='Liked')
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return str(self.quantity)+" "+self.customer.first_name + ' ordering ' + self.product.product_name+' is '+self.status
