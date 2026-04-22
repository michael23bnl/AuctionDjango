from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auctions.urls')),
    path('', include('users.urls')),
    path('', include('user_auctions.urls')),
    path('', include('user_lots.urls')),
]













