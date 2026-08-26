from django.urls import path
from . import views as product_view
urlpatterns=[
    path('all/',product_view.Products_listing.as_view(),name="products"),
    path('<int:pk>/',product_view.product_detail.as_view(),name="detail"),
    path('create/',product_view.product_create.as_view(),name="create"),
    path('delete/<int:pk>/',product_view.product_detail.as_view(),name="delete"),
    path('update/<int:pk>/',product_view.product_detail.as_view(),name="update"),
]