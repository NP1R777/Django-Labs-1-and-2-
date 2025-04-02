from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "name", "description", "country",
                  "quantity", "price", "pictures_url",
                  "id_category", "deleted_at"]
