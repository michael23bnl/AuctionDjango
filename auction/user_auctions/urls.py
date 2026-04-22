from django.urls import path
from . import views

urlpatterns = [
    path('my-auctions/', views.my_auctions, name='my_auctions'),
    path('create/', views.create_auction, name='create_auction'),
    path('edit/<str:auction_id>/', views.edit_auction, name='edit_auction'),
]












