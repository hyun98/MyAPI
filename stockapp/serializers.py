from rest_framework import serializers

from stockapp.models import StockInfo


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = '__all__'
