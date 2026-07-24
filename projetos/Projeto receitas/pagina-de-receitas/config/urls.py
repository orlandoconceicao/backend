from django.contrib import admin

from django.urls import path, include

from django.http import HttpResponse

from recipes_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes_page.urls')),
]
