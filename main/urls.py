from django.urls import path, include
from . import views


urlpatterns = [
    path('links', views.LinkAdd.as_view(), name='links'),
    path('about', views.about, name='about'),
    path('', views.home, name='home'),
]


