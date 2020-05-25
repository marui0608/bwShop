from apps.goods.models import Goods
from django.views.generic import View


class GoodsListView(View):
    def get(self,request):
        # 通过django的view实现商品列表页
        json_list = []
        # 获取所有商品
        goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     # 获取商品的每个字段，键值对形式
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)


        '''
            model_to_dict
            *报错
            Object of type ImageFieldFile is not JSON serializable
            `````````````` add_time `````````````
        
        from django.forms.models import model_to_dict
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)
        '''

        '''
            django serializer
        
        from django.core import serializers
        from django.http import JsonResponse
        import json
        
        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)
        
        '''
        from django.http import HttpResponse
        # 只能转换dict和list类型
        import json
        # 返回json，一定要指定类型，content_type = 'application/json'
        return HttpResponse(json.dumps(json_list),content_type='application/json')