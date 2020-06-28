from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    path('', views.Payment.as_view(), name='Payment'),
    
]
