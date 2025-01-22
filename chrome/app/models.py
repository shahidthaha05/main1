from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    size = models.CharField(max_length=10)  

    def __str__(self):
        return self.size

# Create your models here.
class Product(models.Model):
    pro_id=models.TextField()
    name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()
    size = models.CharField(
        max_length=10,
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')],
        blank=True,
        null=True
    )
    
    



    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


