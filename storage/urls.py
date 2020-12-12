from django.urls import path
from .views import *
app_name = 'storage'
urlpatterns = [
    path('ufile/',upload_file,name='ufile'),
    path('result/',result,name='result'),
]