from django.db import models

# Create your models here.
class Product(models.Model):
	name  = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	#Sbody1 = models.CharField(max_length=2000)
	pub_date = models.DateTimeField(auto_now_add=True)
	#user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.name