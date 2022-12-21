from django.urls import path
from .views import home, sign_up, sign_in

urlpatterns = [
    path('', home, name='home'),
    path('sign-up', sign_up, name='sign-up'),
    path('sign-in', sign_in, name='sign-in')
]
