from django.contrib import admin
from django.urls import path,include
from .views import AddProductView,DisplayProducts,DeleteProducts,EditProductView,DownloadDataView,BulkUpload,GoogleSheetUpload,GetFacebookPageData,GetTwitterData,GetInstagramData

urlpatterns = [
	path('',DisplayProducts.as_view(),name='display_products'),
	path('add/',AddProductView.as_view(),name='add_product'),
	path('delete/<int:id>',DeleteProducts.as_view(),name='delete_product'),
	path('edit/<int:product_id>',EditProductView.as_view(),name='edit_product'),
	path('download/',DownloadDataView.as_view(),name='download_data'),
	path('upload/',BulkUpload.as_view(),name='upload_data'),
	path('sheet_upload/',GoogleSheetUpload.as_view(),name='sheet_upload'),
	path('fb_data/',GetFacebookPageData.as_view(),name='fb_data'),
	path('twitter_data/',GetTwitterData.as_view(),name='instagram_data'),
	path('insta_data/',GetInstagramData.as_view(),name='twitter_data'),

]