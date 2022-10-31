from django.urls import path
from app_media.views import *

urlpatterns = [
    path('upload_media/', upload_file, name='upload_file'),
    path('model_form_upload_file/', model_form_upload),
    path('upload_files/', multi_model_form_upload),
]