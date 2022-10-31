from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('another_login/', views.AnotherLoginView.as_view(), name='another_login'),
    path('logout/', views.logout_view),
    path('another_logout/', views.AnotherLogOut.as_view()),
    path('register/', views.register_view, name='register'),
    path('another_register/', views.another_register_view, name='register'),
]