from django.urls import path
from . import  views
urlpatterns = [
    path('',views.categoryList,name="category.all"),
    path('<int:id>',views.categorydetails,name="category.details"),
    path('New',views.addCategory,name="category.add"),
    path('Delete/<int:id>',views.categoryDelete,name="category.delete"),
    # Update
    path('Update/<int:id>',views.categoryOldData,name="category.oldData"),
    path('UpdateData/<int:id>',views.categoryUpdate,name="category.update"),
]