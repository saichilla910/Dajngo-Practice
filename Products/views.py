from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Product
from .serializers import product_serializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class Products(APIView):

    def get(self, request,pk=None):
        if pk is not None:
            product=get_object_or_404(Product,pk=pk)
            serializer = product_serializer(product, many=False)
        else:
            products = Product.objects.all()
            serializer = product_serializer(products, many=True)
        return Response(serializer.data)
    def post(self,request):
        parser_classes = [MultiPartParser, FormParser]
        serializer=product_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get("Name")
            description=serializer.validated_data.get("description")
            if description is None:
                description=title
            serializer.save()
            return Response(serializer.data)
            