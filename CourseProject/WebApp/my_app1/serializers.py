from collections import OrderedDict
from rest_framework import serializers
from .models import Product, CustomUser, AuthUser, Application


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "description", "country",
                  "quantity", "price", "pictures_url",
                  "id_category", "deleted_at"]
        
        def get_fields(self):
            new_fields = OrderedDict()
            for name, field in super().get_fields().items():
                field.required = False
                new_fields[name] = field
            return new_fields


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["pk", "created_at", "deleted_at", "is_active", "is_progress",
                  "is_close", "is_draft", "is_reject", "quantity_product", "id_product"]


class FullStockSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ["pk", "name", "description", "country",
                  "quantity", "price", "pictures_url",
                  "id_category", "deleted_at"]


class CustomUserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False, required=False)
    is_superuser = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'password', 'is_staff', 'is_superuser']
