from django.db import models

# Create your models here.
class Product(models.Model):
	name  = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	pub_date = models.DateTimeField(auto_now_add=True)
	description= models.TextField(default="")
	stock=models.IntegerField(default=0)
	available=models.NullBooleanField(default=False)
	catagory=models.CharField(max_length=200,default='')
	def __str__(self):
		return self.name

class FileDataModel(models.Model):
    created_date=models.DateTimeField(auto_now=True)
    path=models.FileField(upload_to='data_files/csv')

class FacebookData(models.Model):
	status = models.CharField(max_length=500)
	comment = models.CharField(max_length=500)
	comment_from = models.CharField(max_length=500)
	number_of_likes = models.IntegerField(default=0)

class TwitterData(models.Model):
	id_message = models.BigIntegerField(default=0,null=True)
	message = models.CharField(max_length=200,null=True)
	number_of_likes = models.IntegerField(default=0,null=True)
	posted_by_user = models.CharField(max_length=30,null=True)
	replied_to_user = models.CharField(max_length=30,null=True)
	replied_to_message_id = models.CharField(max_length=200,null=True)