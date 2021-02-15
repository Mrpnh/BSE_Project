from django.urls import path,include
from .views import index,search

urlpatterns = [
    path('',index,name='home'),
    path('search/',search,name='search'),

]