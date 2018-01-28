from .models import Product,FileDataModel



class ProductApi():

	def create(self,name,price,description,stock,category):
		prod=Product()
		prod.name=name
		prod.price=price
		prod.description=description
		prod.stock=stock
		prod.catagory=category
		prod.save()

		return prod


	def get(self,id):
		prod=Product.objects.get(id=id)

		return prod

	def delete(self,id):
		prod=Product.objects.get(id=id)
		prod.delete()

	def edit(self,id,name,price,description,stock,category):
		prod=ProductApi().get(id=id)
		prod.name=name
		prod.price=price
		prod.description=description
		prod.stock=stock
		prod.catagory=category
		prod.save()
		return prod