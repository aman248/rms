from django.urls import path
from .views import upload_file,result,loginpage,registerpage,logoutpage

app_name = 'storage'
urlpatterns = [
    path('ufile/',upload_file,name='ufile'),
    path('result/',result,name='result'),
    path('signup',registerpage,name='register'),
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logout'),
]