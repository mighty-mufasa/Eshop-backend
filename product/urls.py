from django.urls import path
from . import  views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',views.productList,name="product.all"),
    path('<int:productid>',views.productdetails,name="productDetails"),
    path('New',views.addProduct,name="productAdd"),
    path('NewForm',login_required(views.productAddForm),name="product.addForm"),
    path('Delete/<int:id>',views.productDelete,name="product.delete"),
    path('Update/<int:id>',views.productUpdate,name="product.update"),
    # Form Model
    path('NewFormModel',login_required(views.productAddFormModel),name="product.addFormModel"),
    # path('UpdateFormModel/<int:id>',views.productUpdateFormModel,name="product.updateFormModel"),

    # ClassBasedView
    # path('UpdateFormModel/<int:id>',views.ProductUpdate.as_view(),name="product.updateFormModel"),

    # GenericView
    path('UpdateFormModel/<pk>',login_required(views.ProductUpdateGeneric.as_view()),name="product.updateFormModel"),
    path('<pk>',views.ProductDetailsGeneric.as_view(),name="product.detailsFormModel"),
    path('DeleteFormModel/<pk>',login_required(views.ProductDeleteGeneric.as_view()),name="product.deleteFormModel"),
    path('ListFormModel/',views.ProductListGeneric.as_view(),name="product.listFormModel"),
    path('AddFormModel/',login_required(views.ProductAddGeneric.as_view()),name="product.addFormModel"),
]