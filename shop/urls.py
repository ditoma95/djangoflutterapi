from django.urls import path
from shop.views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>', show, name='show')
]
