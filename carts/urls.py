from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('delete/', views.cart_summary, name='cart_delete'),
    path('update/', views.cart_summary, name='cart_update'),
    path('add/', views.cart_add, name='cart_add'),
]
