from django.db import models
from products.models import Product
# Create your models here.
class Cart(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=1)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name