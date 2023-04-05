from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . models import Product, Category, Product_img, Category_img
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect 



def base(request):
    return render(request , 'shop/base.html')

def main(request):
    data = Category.objects.all()
    cat_img = Category_img.objects.all()
    return render( request , 'shop/main.html' , {'data': data , 'cat_img': cat_img } )
    #return render( request , 'shop/main.html' , {'data': data } )

def category(request , id_cat ):
    cat_name = Category.objects.get( category = id_cat)
    data = Product.objects.filter(category = id_cat)
    prod_img = Product_img.objects.filter(id = id_cat)
    return render(request , 'shop/category.html' , {'data': data , "name": cat_name.name , 'prod_img': prod_img } )

def product(request , id_prod):
    data = Product.objects.get(id = id_prod)
    prod_img = Product_img.objects.filter(id = id_prod)
    return render(request , 'shop/product.html' , { "data" : data , 'prod_img': prod_img } )
    

