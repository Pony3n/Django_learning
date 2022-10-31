from django.urls import path
from app_goods.views import *

urlpatterns = [
    path('goods/', items_list),
    path('update_prices', update_price)
]