from django.urls import path,include
from .views import index

urlpatterns = [
    path('',index,name='home'),
    path('search',index,name='search'),

]