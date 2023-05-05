from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.urls
from . import views
from property.views import general, booking

urlpatterns = [
    path('', views.general.home, name='home'),
    path('register', views.general.register, name='register'),
    path('dashboard/', views.general.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('book_room/<int:id>/', views.booking.book_room, name='book_room'),
    path('booking_confirmation/<int:id>/', views.booking.booking_confirmation, name='booking_confirmation'),
    path('logout/', views.general.logout_user, name='logout'),
]