from django.urls import path
from . import views as product_view
urlpatterns=[
    path('all/',product_view.Products.as_view(),name="products"),
    path('<int:pk>/',product_view.Products.as_view(),name="detail"),
    path('create/',product_view.Products.as_view(),name="create"),
]