from django.urls import path
from . import  views
urlpatterns = [
    path('',views.productList,name="product.all"),
    path('<int:productid>',views.productdetails,name="productDetails"),
    path('New',views.addProduct,name="productAdd"),
    path('Delete/<int:id>',views.productDelete,name="product.delete"),
]