from django import forms
from .models import choices

class CreateProductForm(forms.Form):
	name  = forms.CharField(max_length=200)
	price = forms.DecimalField(max_digits=10, decimal_places=2)
	
	description = forms.CharField(max_length=500)
	stock=forms.IntegerField()
	# available=forms.BooleanField(widget=forms.CheckboxInput(),initial=False)
	category=forms.CharField()
	productID=forms.CharField()

class BulkUploadForm(forms.Form):
	file_name= forms.FileField()



class SheetAPIForm(forms.Form):
	"""docstring for SheetAPIForm"""

	sheet_id=forms.CharField(max_length=200)

class BarcodeUploadForm(forms.Form):
	image_name=forms.FileField(label='choose your image')

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField()
	user_type=forms.ChoiceField(choices=choices)
	password = forms.CharField(max_length=32)


class LoginForm(forms.Form):
	email=forms.EmailField(max_length=32)
	password=forms.CharField(max_length=32)

	









	
		
	
