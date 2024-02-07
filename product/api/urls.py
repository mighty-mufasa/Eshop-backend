from django.urls import path
from .views import *

urlpatterns = [
    path('Hello/',Hello,name='hello'),
    path('acceptData/',acceptData,name='acceptData'),
    path('allProducts/',allProducts,name='allProducts'),
    path('<int:id>/',getProduct,name='getProduct'),
    path('addProduct/',addProduct,name='addProduct'),
    path('updateProduct/<int:id>',updateProduct,name='updateProduct'),
    path('deleteProduct/<int:id>',deleteProduct,name='deleteProduct'),

    # Generic View
    path('allProductsGeneric/',allProductsGeneric.as_view(),name='allProductsGeneric'),
]