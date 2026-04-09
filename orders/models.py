from django.db import models
from products.models import Product
# Create your models here.
class Order(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	total_price=models.IntegerField()
	status=models.CharField(max_length=10,default='pending')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.product.name