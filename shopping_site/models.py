from django.db import models
# from .search import ProductIndex

# Create your models here.
from django.contrib.auth.models import User

choices = (
	('admin','admin'),
	('user','user')
	)
class Product(models.Model):
	name  = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	pub_date = models.DateTimeField(auto_now_add=True)
	description= models.TextField(default="")
	stock=models.IntegerField(default=0)
	available=models.NullBooleanField(default=False)
	catagory=models.CharField(max_length=200,default='')
	productID=models.CharField(max_length=220)
	Barcode_Path=models.ImageField(upload_to='data_files/svg', null=True, blank=True)
	barode_id=models.CharField(max_length=220)

	def __str__(self):
		return self.name



class FileDataModel(models.Model):
    created_date=models.DateTimeField(auto_now=True)
    path=models.FileField(upload_to='data_files/csv')
    test_fields=models.IntegerField(default=0)

class ImageDataModel(models.Model):
	created_date=models.DateTimeField(auto_now=True)
	path=models.ImageField(upload_to='data_files/svg')

class UserProfileModel(User):
	user_types = models.CharField(max_length=32,choices=choices)

	




	














    




