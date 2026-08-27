from django.urls import path
from . import views as product_view
from rest_framework.routers import DefaultRouter
from .views import Product_viewsets
# urlpatterns=[
#     # path('all/',product_view.Products.as_view(),name="products"),
#     # path('<int:pk>/',product_view.Products.as_view(),name="detail"),
#     # path('create/',product_view.Products.as_view(),name="create"),
#     # path('delete/<int:pk>/',product_view.Products.as_view(),name="delete"),
#     # path('update/<int:pk>/',product_view.Products.as_view(),name="update"),
# ]
router = DefaultRouter()

router.register("products",Product_viewsets , basename="product")

urlpatterns = router.urls