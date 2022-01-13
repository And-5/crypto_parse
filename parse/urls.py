from django.urls import path
from parse.views import *


urlpatterns = [
    path('', coingecko),
    path('coingecko', coingecko),
    path('create_coingecko', create_coingecko),
    path('cryptorank', cryptorank),
    path('create_cryptorank', create_cryptorank),
]
