from rest_framework import serializers
from cart.models import Cart
class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model=Cart
		fields='__all__'
	def to_representation(self,instance):
		data=super().to_representation(instance)
		request=self.context.get('request')
		data['product_name']=instance.product.name
		data['price']=instance.product.price
		if request:
			data['image']=request.build_absolute_uri(instance.product.image.url)
		else:
			data['image']=instance.image.url
		return data