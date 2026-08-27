from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .forms import profile_Form
from rest_framework.decorators import api_view
from Products.models import Product
# Create your views here.
@login_required()
def home(request):
    context = {'posts': Product.objects.all(),}
    print(context['posts'])
    return render(request, "accounts/home.html", context)

@api_view(['GET','POST'])
@login_required()
def profiles(request,pk=None):
    method=request.method
    if method=='POST':
        form=profile_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=profile_Form()
    return render(request,'Profiles/profile.html',{form:form})
