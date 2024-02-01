from django.urls import path
from . import  views
urlpatterns = [
    path('',views.productList),
    path('<int:productid>',views.productdetails,name="productDetails"),
]