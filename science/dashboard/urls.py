from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashbrd-index'),
    path('predictions/', views.predcitions, name='dashbrd-predictions'),
]
