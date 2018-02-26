from django.contrib import admin
from django.urls import path,include
from .views import AddProductView,DisplayProducts,DeleteProducts,EditProductView,DownloadDataView,BulkUpload,GoogleSheetUpload,GenerateBarCodeView,UploadBarcode,SignupView,LoginView,ProductES,AutoCompleteView,HomePageView,ProductDetailView
from django.contrib.auth.decorators import login_required
urlpatterns = [
	path('',login_required(DisplayProducts.as_view()),name='display_products'),
	path('add/',AddProductView.as_view(),name='add_product'),
	path('delete/<int:id>',DeleteProducts.as_view(),name='delete_product'),
	path('edit/<int:product_id>',EditProductView.as_view(),name='edit_product'),
	path('download/',DownloadDataView.as_view(),name='download_data'),
	path('upload/',BulkUpload.as_view(),name='upload_data'),
	path('sheet_upload/',GoogleSheetUpload.as_view(),name='sheet_upload'),
	path('barcode/<int:product_id>',GenerateBarCodeView.as_view(),name='generate_product'),
	path('barcode_upload/',UploadBarcode.as_view(),name='barcode'),
	path('signup/',SignupView.as_view(),name='signup'),
	path('login/',LoginView.as_view(),name='login'),
	path('api/',ProductES.as_view(),name='api_data'),
	path('autocomplete/',AutoCompleteView.as_view(), name='autocomplete-view'),
	path('products/', login_required(HomePageView.as_view()), name='index-view'),
    path('product',ProductDetailView.as_view(), name='product-detail')

]