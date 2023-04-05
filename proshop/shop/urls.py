from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views



urlpatterns = [
    
    path('base' , views.base , name='Base'),
    path('main/', views.main , name='Main'),
    path('main/category/<int:id_cat>' , views.category , name='Category'),
    path('main/product/<int:id_prod>', views.product , name= 'Product' ),
    
    
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
         