from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_all),
    path('new', views.add_form),
    path('add', views.add),
    path('<int:id>/edit', views.edit),
    path('<int:id>/update',views.update),
    path('<int:id>',views.show_one),
    path('<int:id>/delete', views.delete)
]