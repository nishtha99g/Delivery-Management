from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.searchproducts, name='searchproducts'),
    path('shopkeeper/',views.shopkeeper_view,name='shopkeeper_view'),

]