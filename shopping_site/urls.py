from django.contrib import admin
from django.urls import path,include
from .views import AddProductView,DisplayProducts,DeleteProducts,EditProductView

urlpatterns = [
	path('',DisplayProducts.as_view(),name='display_products'),
	path('add/',AddProductView.as_view(),name='add_product'),
	path('delete/<int:id>',DeleteProducts.as_view(),name='delete_product'),
	path('edit/<int:product_id>',EditProductView.as_view(),name='edit_product')

]