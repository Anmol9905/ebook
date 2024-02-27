from django.urls import path
from .views import index,signup

urlpatterns = [
    path('',index, name='home'),
   path('signup', signup, name='signup'),
    
]
