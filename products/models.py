from tkinter import CASCADE
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'menus'

class Category(models.model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)    
    class Meta:
        db_table = 'categories'

class Drink(models.model):
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description  = models.TextField()
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    class Meta:
        db_table = 'drinks'

class Allergy(models.model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'allergy'

class Allergy_drink(models.model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)    
    drink   = models.ForeignKey('Drink'  , on_delete=models.CASCADE)    
    class Meta:
        db_table = 'allergy_drink'

class Size(models.model):
    name             = models.CharField(max_length=45)
    size_ml          = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = 'sizes'

class Nutrition(models.model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg       = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g        = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g       = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffine_mg      = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink_mg        = models.ForeignKey('Drink', on_delete=CASCADE, null=True)
    size_id         = models.ForeignKey('Size' , on_delete=CASCADE, null=True)
    class Meta:
        db_table = 'nutritions'

class Image(models.model):
    Image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete=CASCADE)
    class Meta:
        db_table = 'images'