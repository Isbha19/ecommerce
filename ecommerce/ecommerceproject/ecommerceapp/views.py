from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Product

# Create your views here.
def Allproducts(request,cslug=None):
    cpage=None
    Productslist=None
    if cslug!=None:
        cpage=get_object_or_404(Category,slug=cslug)
        Productslist=Product.objects.all().filter(category=cpage,available=True)
    else:
        Productslist=Product.objects.all().filter(available=True)
    paginator=Paginator(Productslist,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        Products=paginator.page(page)
    except  (EmptyPage,InvalidPage):
        Products = paginator.page(paginator.num_pages)
    return render(request,"category.html",{'product':Products,"category":cpage})

def productdetails(request,cslug,productslug):
    product=Product.objects.get(category__slug=cslug,slug=productslug)
    return render(request,"productdetails.html",{"product":product})


