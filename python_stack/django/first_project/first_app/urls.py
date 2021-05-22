from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('add2' , views.add2),
    path('destroy', views.destroy)
]
