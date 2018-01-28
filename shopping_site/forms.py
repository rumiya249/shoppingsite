from django import forms

class CreateProductForm(forms.Form):
	name  = forms.CharField(max_length=200)
	price = forms.DecimalField(max_digits=10, decimal_places=2)
	
	description = forms.CharField(max_length=500)
	stock=forms.IntegerField()
	# available=forms.BooleanField(widget=forms.CheckboxInput(),initial=False)
	category=forms.CharField()

class BulkUploadForm(forms.Form):
	file_name= forms.FileField()



class SheetAPIForm(forms.Form):
	"""docstring for SheetAPIForm"""

	sheet_id=forms.CharField(max_length=200)
	
		
	
