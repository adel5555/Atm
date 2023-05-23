# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_for_data_and_card_id, name='card_id'),
    path('card_password/', views.process_for_password, name='password'),
    path('card_withdraw/', views.process_for_withdraw, name='withdraw'),

]