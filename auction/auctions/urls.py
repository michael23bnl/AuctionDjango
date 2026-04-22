from django.urls import path
from . import views

urlpatterns = [
    path('auctions/', views.auction_list, name='auction_list'),
    path('lots/', views.lot_list, name='lot_list'),
    path('bids/', views.bid_list, name='bid_list'),
    path('search/', views.search_lots, name='search_lots'),
    path('', views.home, name='home'),
]








