from .models import Product,FileDataModel, FacebookData, TwitterData



class ProductApi():

	def create(self,name,price,description,stock,category,productID):
		prod=Product()
		prod.name=name
		prod.price=price
		prod.description=description
		prod.stock=stock
		prod.catagory=category
		prod.productID=productID
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


class FacebookApi(object):

	def create_status(self,message,comment,comment_from,no_of_likes):
		facebook_data = FacebookData.objects.get_or_create(
			status= message,
			number_of_likes=no_of_likes,
			
			comment_from=comment_from,
			comment=comment,)


		# data.status = message
		# data.comment = comment
		# data.comment_from = comment_from
		# data.number_of_likes = no_of_likes
		# data.save()
		# return data
		
	# def create_status(self,message,comment,comment_from,no_of_likes):
	# 	data = FacebookData()
	# 	data.status = message
	# 	data.comment = comment
	# 	data.comment_from = comment_from
	# 	data.number_of_likes = no_of_likes
	# 	data.save()
	# 	return data

class TwitterApi(object):
		
	def create_status(self,id_message, message, likes, posted_by_user, replied_to_user, replied_to_message_id):
		#data = TwitterData
		twitter_data=TwitterData.objects.get_or_create(
			id_message=id_message,
			defaults={
			'message':message,
			'number_of_likes':likes,
			'posted_by_user':posted_by_user,
			'replied_to_user':replied_to_user,
			'replied_to_message_id':replied_to_message_id,

			}
			)
		
	