from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserFormView.as_view()),
    path('', views.main)
]