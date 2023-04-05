from django.contrib import admin
from .models import Product, Category, Product_img , Category_img


admin.site.register(Product)
admin.site.register(Product_img)
admin.site.register(Category)
admin.site.register(Category_img)

