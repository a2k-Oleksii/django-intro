from django.urls import path
from .views import add_product, products_details

urlpatterns = [
    path('/add', add_product, name='add_product'),
    path('/<int:id>', products_details, name='products_details')
]