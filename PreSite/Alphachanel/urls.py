from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_chanel, name='main_chanel'),
    path('second_chanel/', views.second_chanel, name='second_chanel'),
    path('third_chanel/', views.third_chanel, name='third_chanel'),
    path('fourth_chanel/', views.fourth_chanel),
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('regions/', views.About.as_view()),
    path('advertisement/', views.adv_list),
    path('advertisment_list/', views.AdvertismentListView.as_view())
]