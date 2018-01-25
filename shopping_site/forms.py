
class CreateProductForm(forms.ModelForm):
	name  = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	#Sbody1 = models.CharField(max_length=2000)
	
	description = models.CharField(max_length=500)
	stock = models.PositiveInteger()
	
	class Meta:
		model = BlogList
		fields = ['name','price', 'description','stock',]