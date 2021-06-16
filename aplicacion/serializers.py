from rest_framework import serializers
from . import models


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sale

        fields = ['id', 'price', 'client', 'created_at', 'updated_at']
