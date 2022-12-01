from django.urls import path

from .import views
app_name='ecommerce'

urlpatterns = [
    path('',views.Allproducts,name='Allproducts'),
    path('<slug:cslug>/', views.Allproducts, name='Allproductsbycategory'),
    path('<slug:cslug>/<slug:productslug>', views.productdetails, name='productdetails'),

]