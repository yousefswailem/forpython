from django.urls import path
from . import views
urlpatterns = [
    path('',views.guess),
    path('guess',views.result),
    path('reset',views.reset),
    path('username',views.send_name),
]