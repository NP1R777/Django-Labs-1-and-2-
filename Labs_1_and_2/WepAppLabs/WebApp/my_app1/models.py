from django.db import models
from datetime import timezone
from django.contrib import admin


class Category(models.Model):
    class Meta:
        db_table = 'category'
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class User(models.Model):
    class Meta:
        db_table = 'user'
    
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now_add=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=16, null=False)
    phone_number = models.CharField()
    refresh_token = models.CharField()
    id_user = models.ForeignKey(Category, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class Product(models.Model):
    class Meta:
        db_table = 'product'
    
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    country = models.CharField(null=True)
    pictures_url = models.URLField(null=False)
    quantity = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now_add=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.id_category.name


class Application(models.Model):
    class Meta:
        db_table = 'application'
    
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now_add=True, null=True)
    deleted_at = models.DateField(auto_now_add=False, null=True)
    is_active = models.BooleanField(default=False)
    is_progress = models.BooleanField(default=False)
    is_close = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    is_reject = models.BooleanField(default=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_product = models.IntegerField(default=1, null=False)


admin.site.register([Category, User, Product, Application])
