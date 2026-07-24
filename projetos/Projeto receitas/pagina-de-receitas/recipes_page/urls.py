from django.urls import path

from recipes_page import views

urlpatterns = [
    path('', views.home, name='home'),
]
