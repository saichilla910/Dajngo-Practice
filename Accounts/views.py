from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Products.models import Product
# Create your views here.
@login_required()
def home(request):
    context = {'posts': Product.objects.all(),}

    print(context['posts'])

    return render(request, "accounts/home.html", context)