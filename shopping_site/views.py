from django.shortcuts import render,render_to_response,HttpResponseRedirect

# Create your views here.

from django.views.generic import TemplateView,FormView,View

from .forms import CreateProductForm
from .models import Product

class AddProductView(FormView):
	template_name='add_product.html'
	form_class = CreateProductForm


	def get(self,request,*args,**kwargs):
		context={}
		form=self.form_class()
		context['form'] = form
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		data=request.POST.copy()
		print(data,"djkahdkjahjkdhkajhd")
		form=self.form_class(data)
		if form.is_valid():
			prod=Product()
			prod.name=data.get('name')
			prod.price=data.get('price')
			prod.description=data.get('description')
			prod.stock=data.get('stock')
			prod.available=data.get('available')
			prod.save()
			return HttpResponseRedirect('/shop/')

class DisplayProducts(TemplateView):
	template_name='display_products.html'


	def get(self,request,*args,**kwargs):
		prod_obj=Product.objects.all()
		context={}
		context['prod']=prod_obj
		return self.render_to_response(context)

class DeleteProducts(FormView):
    template_name='display_products.html'


    def post(self,request,*args,**kwargs):
    	data=request.POST.copy()
    	print(data,"delete_data")
    	dele_id=data['dele_id']
    	prod=Product.objects.get(id=dele_id)
    	prod.delete()
    	return HttpResponseRedirect('/shop/')
class EditProductView(FormView):
	form_class=CreateProductForm
	template_name='edit_products.html'


	def get(self,request,*args,**kwargs):
		context={}
		edit_id=kwargs['product_id']
		prod=Product.objects.get(id=edit_id)
		print(edit_id,"edit"*11)
		initial_data={'name':prod.name,'price':prod.price,'stock':prod.stock,'description':prod.description,'category':prod.catagory}
		form=self.form_class(initial=initial_data)
		context['form']=form
		context['id']=prod.id
		return self.render_to_response(context)
    
	def post(self,request,*args, **kwargs):
		data=request.POST.copy()
		edit_id=data.get('edit_ids')
		print(data)
		form=self.form_class(data)
		if form.is_valid():
			prod=Product.objects.get(id=edit_id)
			prod.name=data.get('name')
			prod.price=data.get('price')
			prod.description=data.get('description')
			prod.stock=data.get('stock')
			prod.category=data.get('category')
			prod.save()
			return HttpResponseRedirect('/shop')











