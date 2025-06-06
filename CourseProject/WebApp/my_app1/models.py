from django.db import models
from datetime import timezone
from django.contrib import admin
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin


class Category(models.Model):
    class Meta:
        db_table = 'category'
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(models.Model):
    class Meta:
        db_table = 'user'
    
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now_add=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16, null=False)
    phone_number = models.CharField()
    refresh_token = models.CharField()
    id_user = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        managed = False
        db_table = 'auth_user'


class Product(models.Model):
    class Meta:
        db_table = 'product'
    
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    country = models.CharField(null=True)
    pictures_url = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now_add=True, null=True)
    deleted_at = models.DateField(null=True, blank=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()
    
    # def __str__(self):
    #     return self.name


class Application(models.Model):
    class Meta:
        db_table = 'application'
    
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateField(auto_now_add=False, null=True)
    is_active = models.BooleanField(default=False, null=True)
    is_progress = models.BooleanField(default=False)
    is_close = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    is_reject = models.BooleanField(default=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity_product = models.IntegerField(null=False)


class NewUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email адрес"), unique=True)
    password = models.CharField(max_length=500, verbose_name="Пароль")
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateField(auto_now_add=False, null=True)
    is_superuser = models.BooleanField(default=False, verbose_name="Является ли пользователь админом?")
    list_application = models.JSONField(default=list)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Измените это значение
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Измените это значение
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "email"

    objects = NewUserManager()


class Basket(models.Model):
    class Meta:
        db_table = 'basket'
    
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    list_products = models.JSONField(default=list)


admin.site.register([Category, User, Product, Application,
                     CustomUser, AuthUser, Basket])
