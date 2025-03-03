from django.contrib import admin
from django.urls import path
from Hotel import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('RoomList/', views.RoomList, name='RoomList'),
    path('RoomDetail/<id>', views.RoomDetail, name='RoomDetail'),
    path('RoomUpdate/<id>/', views.RoomUpdate, name='RoomUpdate'),
    path('RoomDelete/<id>/', views.RoomDelete, name='RoomDelete'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('bookingDelete/<id>/', views.bookingDelete, name='bookingDelete'),
    path('manage_rooms/', views.manage_rooms, name='manage_rooms'),
    path('RoomAdd/', views.RoomAdd, name='RoomAdd'),
    path('usersUpdate/<id>/', views.usersUpdate, name='usersUpdate'),
    path('booking/<id>', views.booking, name='booking'),
    path('payment/<id>/', views.payment, name='payment'),
    path('booking_history/', views.booking_history, name='booking_history'),
    path('usersDelete/<id>/', views.usersDelete, name='usersDelete'),
    path('usersDetail/<id>/', views.usersDetail, name='usersDetail'),
    path('AddCategory/', views.AddCategory, name='AddCategory'),
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
