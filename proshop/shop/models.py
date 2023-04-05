from django.db import models

class Product(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image =  models.ForeignKey('product_img' , on_delete=models.CASCADE ,  blank=True , null=True)
        
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length= 200)
    image =  models.ForeignKey('category_img' , on_delete=models.CASCADE ,  blank=True , null=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product_img(models.Model):
    name = models.CharField(max_length= 200)
    img = models.ImageField(upload_to="shop\static\shop\prod_img" , blank=True , null=True)

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

    def __str__(self):
        return self.name
    
class Category_img(models.Model):
    name = models.CharField(max_length= 200)
    img = models.ImageField(upload_to="shop\static\shop\cat_img" , blank=True , null=True)

    class Meta:
        verbose_name = 'Фото категории'
        verbose_name_plural = 'Фото категорий'

    def __str__(self):
        return self.name
    
        