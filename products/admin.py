from django.contrib import admin
from .models import product,order,review

# Register your models here.
admin.site.register(product)
admin.site.register(order)
admin.site.register(review)