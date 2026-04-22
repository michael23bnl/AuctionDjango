from django.urls import path
from . import views

urlpatterns = [
    path('my-lots/', views.my_lots, name='my_lots'),
    path('create-lot/', views.create_lot, name='create_lot'),
    path('edit-lot/<str:lot_id>/', views.edit_lot, name='edit_lot'),
]

