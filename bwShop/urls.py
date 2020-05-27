from django.urls import path,include
from django.views.static import serve

import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from bwShop.settings import MEDIA_ROOT
from apps.goods.views import GoodsListViewSet,CategoryViewSet
from apps.users.views import SmsCodeViewset


router = routers.DefaultRouter()
router.register('goods',GoodsListViewSet)
router.register('categorys',CategoryViewSet,basename='categorys')
router.register('code',SmsCodeViewset,basename='code')

schema_view = get_schema_view(title='corejson')
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    # 文件上传路径
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # path('goods/',GoodsListViewSet.as_view(),name='goods-list'),
    path(r'',include(router.urls)),
    # token 路由
    path('api-token-auth',views.obtain_auth_token),
    # jwt 路由
    path('login/',obtain_jwt_token),
    # DRF 路由
    path('api-auth/',include('rest_framework.urls')),
    # 文档路由
    path('docs',include_docs_urls(title='DRF文档')),
    path('schema/',schema_view),
]