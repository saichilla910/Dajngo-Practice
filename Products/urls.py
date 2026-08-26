from django.urls import path
from . import views as product_view
urlpatterns=[
    path('all/',product_view.Products,name="products"),
    path('<int:pk>/',product_view.Products,name="detail"),
    path('create/',product_view.Products,name="create"),
    path('delete/<int:pk>/',product_view.product_detail,name="delete"),
    path('update/<int:pk>/',product_view.product_detail,name="update"),
]