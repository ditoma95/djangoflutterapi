from django.contrib import admin
from django.urls import path, include
from authen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('connexion', views.connexion, name="connexion"),
    path('inscription', views.inscription, name="inscription"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
]
