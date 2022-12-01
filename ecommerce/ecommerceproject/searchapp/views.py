from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q

# Create your views here.
def searchresult(request):
    query=None
    product=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,"search.html",{'product':product,'query':query})
