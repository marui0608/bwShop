from rest_framework import serializers

from apps.goods.models import Goods,GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖原来只有ID的类别
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'



