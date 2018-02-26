from __future__ import print_function

from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse

# Create your views here.

from django.views.generic import TemplateView,FormView,View

<<<<<<< HEAD
from .forms import CreateProductForm,BulkUploadForm,SheetAPIForm
from .models import Product,FileDataModel, FacebookData, TwitterData
import csv
from .api import ProductApi, FacebookApi, TwitterApi
=======
from .forms import CreateProductForm,BulkUploadForm,SheetAPIForm,BarcodeUploadForm,SignupForm,LoginForm
from .models import Product,FileDataModel,ImageDataModel,UserProfileModel
import csv
import json
from .api import ProductApi
>>>>>>> bc65a24b008b8b8463de5502abfcdf87bb321000



import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import requests

import tweepy, json
from tweepy import OAuthHandler
from urllib.request import urlopen
from instagram.client import InstagramAPI

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

import barcode
from pyzbar.pyzbar import decode
from PIL import Image
from django.core.files.storage import FileSystemStorage

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
	image_form=BarcodeUploadForm

	def get(self,request,*args,**kwargs):
		prod_obj=Product.objects.all()
		form=self.form_class()
		form_sheet=self.form_class2()
		img_code=self.image_form()
		context={}
		context['prod']=prod_obj
		context['form2']=form
		context['sheetform'] = form_sheet
		context['form_img']=img_code
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
		print(ean,"aaaaa")
		filename = ean.save('/home/rumiya/workspace/mysite/data_files/svg/'+str(prod_obj.name)+str(prod_obj.productID))
		print(filename,dir(filename))
		prod_obj.Barcode_Path=filename
		prod_obj.barode_id=ean
		prod_obj.save() 
		return HttpResponseRedirect('/shop')

class UploadBarcode(TemplateView):
	print("inside ")
	image_form=BarcodeUploadForm
	def post(self,request,*args,**kwargs):
		data=request.POST.copy()
		print("data1",data)
		form=self.image_form(data,request.FILES)
		if form.is_valid():
			img_model=ImageDataModel()
			img_model.path=request.FILES.get('image_name')
			print("path3",img_model.path)
			img_model.save()
			file_url=img_model.path.url
			print("path",file_url)
			decode(Image.open('/home/rumiya/workspace/mysite/data_files/svg/'))
		return HttpResponseRedirect('/shop')

class SignupView(FormView):
    template_name='signup.html'
    form_class = SignupForm	

    def get(self,request,*args,**kwargs):
        context={}
        form=self.form_class()
        context['form'] = form
        return self.render_to_response(context)	
    def post(self,request,*args,**kwargs):
    	data=request.POST.copy()
    	print (data,"jghjghjghjghjghjg")
    	form=self.form_class(data)
    	if form.is_valid():
    		usr_obj = UserProfileModel()
    		usr_obj.user_types = data.get('user_type')
    		usr_obj.first_name = data.get('first_name')
    		usr_obj.last_name = data.get('last_name')
    		usr_obj.email = data.get('email')
    		usr_obj.username = data.get('email')
    		usr_obj.set_password(data.get('password'))
    		usr_obj.save()
    	return HttpResponseRedirect('/shop/signup')

class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm


	def get(self,request,*args,**kwargs):
		context={}
		form=self.form_class()
		context['form'] = form
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		data=request.POST.copy()
		print(data)
		email=data.get('email')
		usr_obj = UserProfileModel.objects.get(email=email)
		if usr_obj:
			login(usr_obj,request)



			
# class UploadBarcode(TemplateView):
# 	def post(self,request,*args,**kwargs):
# 		uploadedFile=handle_uploaded_file(request.FILES['image_name'])
# 		return HttpResponseRedirect('/shop')

		
# 		def handle_uploaded_file(filename):
# 			if not os.path.exists('upload/'):
# 				os.mkdir('upload/')
# 			filePath = 'upload/' + filename
# 			print("file path",filepath)
# 			return filePath
 
    	# with open(filePath, 'wb+') as destination:
     #    	for chunk in file.chunks():
     #    	    destination.write(chunk)

class ProductES(View):
    def get(self,request,*args,**kwargs):
        # print (request.GET)
        product_obj=Product.objects.all()
        with open('test.json','w') as f:
	        prod_dictionary={}
	        lis_data=[]
	        for i in product_obj:
	            new_dictionary={}
	            new_dictionary["name"]=i.name
	            new_dictionary['price']=int(i.price)
	            # new_dictionary['pub_date']=i.pub_date
	            new_dictionary['description']=i.description
	            new_dictionary['stock']=i.stock
	            new_dictionary['available']=i.available
	            new_dictionary['catagory']=i.catagory
	            new_dictionary['productID']=i.productID
	            # new_dictionary['Barcode_Path']=i.Barcode_Path
	            new_dictionary['barode_id']=i.barode_id
	            f.write('{"index":{"_id":%s}}'%i.id)
	            f.write('\n')
	            f.write(json.dumps(new_dictionary))
	            f.write('\n')
	            lis_data.append(new_dictionary)
        	prod_dictionary={'data':lis_data}
        	s=json.dumps(prod_dictionary)
        return HttpResponse(s)










































 
 
			
		
























class GetFacebookPageData(TemplateView):
	#token = 'EAACEdEose0cBALfPIkYEzdGfW25zrU9bxADYbmjLPaPQjZAojr2eqKCDFSMtnTTsVHy0DHPE4oxUZBtNNOqZBKGTQSS6jpFg48EeFpVkg2QyUiLmqiocpcjAuDDDQDVXbe93mj6MDhO3yoscrewWwZA3dhHJe9NmCwRh83NIIubq3jx9ucWUU1ZAyycDhdWQwYrvZBNvLlZBAZDZD'

	#page = 'https://graph.facebook.com/v2.12/apibyheena?fields=posts{message,likes,comments}&access_token='+token
	# def get(self,request,*args,**kwargs):
	# page2 = 'https://graph.facebook.com/v2.12/me?access_token='+token
	
	template_name='social_media_data.html'

	def get(self, url, params=None, **kwargs):
		
		token = 'EAACEdEose0cBAEpTNiYG681XwoQ0tChDlyo5fhZCVPdcXh5kxUKYhMgiOETFDlBNk82PYywVSYRAtzR6igbHz3RwZCLI1b6s3xCmlKj1o0nuihO5vKpJc5GClsI7NVzMD427imBtIuniGApARxrVJRsz6jZBsN0IWaZBEMkN8AMkxRr5hpzlcPR9b8ItX60k9LBdsoZBN6gZDZD'

		page = 'https://graph.facebook.com/v2.12/apibyheena?fields=posts{message,likes,comments}&access_token='+token

		page_details = requests.get(page)
		apiResponse = page_details.text		
		titles = page_details.json()
		#print("single value@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:",titles)
		posts = titles['posts']
		print("posts:!!!!!!!!!!!!!!!!!!!!!!!!!!",posts)
		data = posts['data']
		print("data *************:",data)
		print("#########################################")
		
		for i,r in enumerate(data):
			#print "state=%s" %r['address'][1]

			message = r["message"]
			likes = r["likes"]

			print("message=",message)
			print("likes=",likes)
			comments = r['comments']			
			no_of_likes = len(likes['data']) 
			print("number of likes", no_of_likes)
			length = len(comments['data'])
			
			for j in range(0,length):
				print("comment:",comments['data'][j]['message'])				
				comment = comments['data'][j]['message']
				print("commenttype:",type(comments))				
				comment_from = comments['data'][j]['from']['name']
				print("comment_from:", comment_from)
				FacebookApi().create_status(message, comment, comment_from, no_of_likes)
			data_obj= FacebookData.objects.all()
			context={}
			context['data'] = data_obj
		return self.render_to_response(context)
					
			#print("l:",likes_list['data'][0]['name'])
			#print("l2:",likes_list['data'][1]['name'])
			# for i, r in enumerate(likes_list):
			#     print("likes_lists:", r['data'])

class GetTwitterData(TemplateView):
	template_name='twitter_data.html'
	def get(self, url, params=None, **kwargs):
		consumer_key = '5UOgWCCYSHwFMI5UoRB0YzZGD'
		consumer_secret = 'PR9WgJSZjgGXy3d1Cx6Gfy0SETZpKXnJUOwu39hKEJABJeJRmV'
		access_token = '4803005483-QbGO0tkMnQStD0ZcT2APEPoazHCSXPlGkVOWNvW'
		access_secret = 'cDtlPPrHedPkwEBpb9FXesXeoJq2V9KCNFX3oVRkG8tJQ'
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)
		api = tweepy.API(auth)
		for status in tweepy.Cursor(api.home_timeline).items(5):
			# status_id = json.dumps(status._json['id'])
			# # status_id = status._json['id']
			# print("status id",status_id)
			# status = json.dumps(status._json['text'])
			# print("status :",status)
			# print("posted by###############:",status._json['user']['screen_name'])
			replied_to_message_id = json.dumps(status._json['in_reply_to_status_id'])
			print("replied_to_status_id", replied_to_message_id)
			#print("replied_type", type(replied_to_message_id))
			replied_to_user = json.dumps(status._json['in_reply_to_screen_name'])
			print("replied_to:", replied_to_user)

			likes = json.dumps(status._json['favorite_count'])
			print("likes:",likes)
			print("likes-type:",type(likes))
			posted_by_user = json.dumps(status._json['user']['screen_name'])
			print("posted by", posted_by_user)
			id_message = json.dumps(status._json['id'])
			print("status id",id_message)
			message = status._json['text']
			print("status :",message)
			TwitterApi().create_status(id_message, message, likes, posted_by_user, replied_to_user, replied_to_message_id)
		data_obj= TwitterData.objects.all()
		context={}
		context['data'] = data_obj
		return self.render_to_response(context)
		#return HttpResponseRedirect('/shop')

			
			# replied_to = json.dumps(status._json['in_reply_to_screen_name'])
			# print("replied_to:", replied_to)
			

			# # TwitterApi().create_status(status._json['id'], status._json['text'], status._json['favorite_count'], status._json['user']['screen_name'], status._json['in_reply_to_screen_name'],status._json['in_reply_to_status_id'])

			# # response= status._json
			# # apiResponse = response
			# # json_data = json.dumps(apiResponse)
			# # #print("res",json_data)
			# # # #val = json.loads('status._json')

			# # status_id = status._json['id']
			# # print("status id:",status_id)
			# # status = status._json['text']
			# # print("status :",status)
			# #likes = status._json['favorite_count']
			# #print("likes:",status._json['favorite_count'])
			# #posted_by = status._json['user']['screen_name']
			# # replied_to = status._json['in_reply_to_screen_name']
			# # replied_to_status_id = status._json['in_reply_to_status_id']
			# # TwitterApi().create_status(status_id, status, likes, posted_by, replied_to, replied_to_status_id)
			# print("status id###############:",status._json['id'])
			# print("status ###############:",status._json['text'])
			# print("likes ###############:",status._json['favorite_count'])
			# print("posted by###############:",status._json['user']['screen_name'])
			# print ("replied to:#########",status._json['in_reply_to_screen_name'])
			# print ("replied to status id:#########",status._json['in_reply_to_status_id'])
		
class GetInstagramData(TemplateView):
	def get(self, url, params=None, **kwargs):
		testurl='https://api.instagram.com/v1/users/self/media/recent/?access_token=2351144425.10312b6.4e0b3d65c1774ee8aeb807e9ff77280a'
		response = urlopen(testurl)
		apiResponse = response.read()
		json_data = json.dumps(apiResponse)
		print("insta json:",json_data)
		return HttpResponseRedirect('/shop')
	# def get(self, url, params=None, **kwargs):
	# 	access_token = "2351144425.10312b6.4e0b3d65c1774ee8aeb807e9ff77280a"
	# 	client_secret = "114973dfa6e146788a42c4518ac697b4"
	# 	api = InstagramAPI(access_token=access_token, client_secret=client_secret)
	# 	recent_media, next_ = api.user_recent_media(user_id="2351144425", count=10)
	# 	print("recentmedia:",recent_media)
	# 	# for media in recent_media:
	# 	# 	print("media:",media.caption.text)
	# 	return HttpResponseRedirect('/shop')



	