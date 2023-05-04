from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.urls
from . import views
from property.views import general, booking

urlpatterns = [
    path('', views.general.home, name='home'),
    path('register', views.general.register, name='register'),
    #path('login/', login_page , name='login_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('book_room/<int:id>/', views.booking.book_room, name='book_room'),
]