from __future__ import print_function

from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse

# Create your views here.

from django.views.generic import TemplateView,FormView,View

from .forms import CreateProductForm,BulkUploadForm,SheetAPIForm
from .models import Product,FileDataModel
import csv
from .api import ProductApi



import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

import barcode

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

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
		name=data.get('name')
		price=data.get('price')
		description=data.get('description')
		stock=data.get('stock')
		category=data.get('category')
		productID=data.get('productID')
		form=self.form_class(data)
		if form.is_valid():
			prod=ProductApi().create(name,price,description,stock,category,productID)
			return HttpResponseRedirect('/shop/')

class DisplayProducts(TemplateView):
	template_name='display_products.html'
	form_class= BulkUploadForm
	form_class2=SheetAPIForm


	def get(self,request,*args,**kwargs):
		prod_obj=Product.objects.all()
		form=self.form_class()
		form_sheet=self.form_class2()
		context={}
		context['prod']=prod_obj
		context['form2']=form
		context['sheetform'] = form_sheet
		return self.render_to_response(context)


	# def post(self,request,*args,**kwargs):
	# 	data=request.POST.copy()
	# 	print(data,"post_data")
	# 	form=self.form_class(data,request.FILES['file_name'])
	# 	file_name = request.FILES['file_name']
	# 	print (file_name.read())
	# 	if form.is_valid():
	# 		csv_obj=csv.reader(file_name.read(),'rU')
	# 		for i in csv_obj:
	# 			print (i)

class DeleteProducts(FormView):
    template_name='display_products.html'


    def post(self,request,*args,**kwargs):
    	data=request.POST.copy()
    	print(data,"delete_data")
    	dele_id=data['dele_id']
    	prod=ProductApi().delete(id=dele_id)
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
		name=data.get('name')
		price=data.get('price')
		description=data.get('description')
		stock=data.get('stock')
		category=data.get('category')
		form=self.form_class(data)
		if form.is_valid():
			prod=ProductApi().edit(edit_id,name,price,description,stock,category)
			prod.save()
			return HttpResponseRedirect('/shop')


class DownloadDataView(View):
	def get(self,request,*args,**kwargs):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=test.csv'
		csv_writer=csv.writer(response)


		prod=Product.objects.all()
		for i in prod:
			append_list=[]
			append_list.append(i.name)
			append_list.append(i.description)
			append_list.append(i.price)
			append_list.append(i.stock)
			csv_writer.writerow(append_list)
		return response

class BulkUpload(TemplateView):
    form_class=BulkUploadForm
    def post(self,request,*args,**kwargs):
        data=request.POST.copy()
        print (data, "jjj",request.FILES)
        form=self.form_class(data,request.FILES)
        if form.is_valid():
           file1=FileDataModel()
           file1.path=request.FILES.get('file_name')
           file1.save()
           filename=file1.path.url
           print(filename)
           with open(filename) as f:
               csv_obj=csv.reader(f) 
               for i in csv_obj:
                   print (i)
                   prod=ProductApi().create(i[0],i[2],i[1],i[3],i[4],i[5])
               return HttpResponseRedirect('/shop')

        else:
        	file1.delete()
        	return HttpResponseRedirect('/shop')

class GoogleSheetUpload(TemplateView):

	form_class=SheetAPIForm

	def get_credentials(self):
    
		home_dir = os.path.expanduser('~')
		credential_dir = os.path.join(home_dir, '.credentials')
		if not os.path.exists(credential_dir):
			os.makedirs(credential_dir)
		credential_path = os.path.join(credential_dir,'sheets.googleapis.com-python-quickstart.json')

		store = Storage(credential_path)
		credentials = store.get()
		if not credentials or credentials.invalid:
			flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
			flow.user_agent = APPLICATION_NAME
			if flags:
				credentials = tools.run_flow(flow, store, flags)
			else: # Needed only for compatibility with Python 2.6
				credentials = tools.run(flow, store)
			print('Storing credentials to ' + credential_path)
		return credentials

	def post(self,request,*args,**kwargs):
		data=request.POST.copy()
		print(data)
		form=self.form_class(data)
		if form.is_valid():
			sheet_id=data.get('sheet_id')
			credentials = self.get_credentials()
			http = credentials.authorize(httplib2.Http())
			discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
			service = discovery.build('sheets', 'v4', http=http,discoveryServiceUrl=discoveryUrl)
			spreadsheetId = sheet_id
			rangeName = 'Sheet1!A1:E9'
			result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
			print(result,"dskfhlksdjfklsdjlkfjskldjfklsdjf")
			values = result.get('values', [])
			print(values,"values")
			if not values:                                                                                                                                               
				print('No data found.')
			else:
				print('Name, Major:')
				for row in values:
					print('%s, %s ,%s, %s,%s' % (row[0], row[1],row[2],row[3],row[4],row[5]))
					name=row[0]
					price=row[2]
					description=row[1]
					stock=row[3]
					category=row[4]
					product_id=row[5]
					prod=ProductApi().create(name,price,description,stock,category,productID)

				return HttpResponseRedirect('/shop')
class GenerateBarCodeView(TemplateView):

	def post(self,request,*args,**kwargs):
		print(kwargs,"dsfdsfdfdsf")
		product_id=kwargs.get('product_id')
		prod_obj=ProductApi().get(id=product_id)
		ean = barcode.get('ean13',str(prod_obj.productID))
		filename = ean.save('/home/rumiya/workspace/mysite/data_files/svg/'+str(prod_obj.name)+str(prod_obj.productID))
		print(filename,dir(filename))
		prod_obj.Barcode_Path=filename
		prod_obj.save()
		return HttpResponseRedirect('/shop')


         
































