from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Product
from .serializers import product_serializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics

# class Products(APIView):

#     def get(self, request,pk=None):
#         if pk is not None:
#             product=get_object_or_404(Product,pk=pk)
#             serializer = product_serializer(product, many=False)
#         else:
#             products = Product.objects.all()
#             serializer = product_serializer(products, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         parser_classes = [MultiPartParser, FormParser]
#         serializer=product_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title=serializer.validated_data.get("Name")
#             description=serializer.validated_data.get("description")
#             if description is None:
#                 description=title
#             serializer.save()
#             return Response(serializer.data)


            
##### function based View for managing the CURD #####################
# @api_view(['GET','POST'])
# def Products(request,pk=None):
#     method=request.method
#     if method=='GET':
#         if pk is not None:
#             product=get_object_or_404(Product,pk=pk)
#             serializer = product_serializer(product, many=False)
#             return Response(serializer.data)
#         products=Product.objects.all()
#         serializer=product_serializer(products,many=True)
#         return Response(serializer.data)
#     if method=='POST':
#         serializer=product_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title=serializer.validated_data.get("Name")
#             description=serializer.validated_data.get("description")
#             if description is None:
#                 description=title
#             serializer.save()
#             return Response(serializer.data)

# @api_view(["PUT", "PATCH", "DELETE"])
# def product_detail(request, pk):

#     product = get_object_or_404(Product, id=pk)

#     # DELETE
#     if request.method == "DELETE":
#         product.delete()
#         return Response(
#             {"message": "Product deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )

#     # UPDATE
#     serializer = product_serializer(
#         product,
#         data=request.data,
#         partial=(request.method == "PATCH")
#     )

#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     return Response(serializer.data)

##### generic views for managing the  manging the CURd ##############

class Products_listing(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = product_serializer


class product_create(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = product_serializer
class product_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = product_serializer
    lookup_field='pk'