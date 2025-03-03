from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import *
from django.contrib import messages 

def home (request):
    return render(request,'home.html')

def RoomList (request):
    rooms = Room.objects.all()
    context = {'rooms':rooms,}
    return render(request,'Hotel/RoomList.html',context)

def RoomDetail(request, id): 
    room = Room.objects.get(room_number = id)
    context = {'room': room}
    return render(request, "Hotel/RoomDetail.html", context)

def RoomUpdate(request, id):
    room = Room.objects.get(room_number = id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('manage_rooms')
    else:
        form = RoomForm(instance=room)
        
    context = {'form':form}
    return render(request, 'Hotel/RoomUpdate.html', context)

def RoomDelete(request, id):
    room = Room.objects.get(room_number = id)
    if request.method == 'POST':
        room.delete()
        return redirect('manage_rooms')
    else:
        context = {'room':room}
        return render(request, 'Hotel/RoomDelete.html', context)

def register(request):
    if request.method == "POST": 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    if request.method == "POST":  
        logout(request)
        return redirect('home')  
    return redirect('home')  

def profile(request):
    customer_profile = None
    if hasattr(request.user, 'customerprofile'):
        customer_profile = request.user.customerprofile
    
    context = {
        'user': request.user,
        'customer_profile': customer_profile
    }
    return render(request, 'profile.html', context)

def manage_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'Hotel/manage_rooms.html', context)

def manage_bookings(request):
    bookings = Booking.objects.filter(status='จองแล้ว')  
    context = {'bookings': bookings}
    return render(request, 'Hotel/manage_bookings.html', context)

def booking(request, id):
    room = get_object_or_404(Room, room_number=id)  
    form = BookingForm(initial={'room': room})  
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.customer = request.user
            
            booking.save()
            form.save()
            
            return redirect('payment', id=booking.bid) 
    
    else:
        form = BookingForm()
     
    context = {'form': form, 'room': room}
    return render(request, "Hotel/booking.html", context)

def manage_users (request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request,'Hotel/manage_users.html',context)

def RoomAdd(request):
    if request.method == 'POST':
        print(request.FILES) 
        form = RoomForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, "เพิ่มห้องพักเรียบร้อยแล้ว!")
            return redirect('manage_rooms')
    else:
        form = RoomForm()
    context = {'form': form}
    return render(request, 'Hotel/RoomAdd.html', context)


def usersUpdate(request, id):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "อัปเดตข้อมูลสำเร็จ!")
            return redirect('manage_users')
        else:
            messages.error(request, "อัปเดตข้อมูลไม่สำเร็จ กรุณาตรวจสอบข้อมูล")
    else:
        form = CustomUserChangeForm(instance=user)
    
    context = {'form': form, 'user': user}
    return render(request, 'Hotel/usersUpdate.html', context)

def payment(request, id):
    booking = Booking.objects.get( bid=id)
    room = booking.room
    nights = (booking.check_out_date - booking.check_in_date).days
    
    total_price = nights * room.price

    if request.method == "POST" and request.FILES.get("payment_slip"):
        payment_id = str(uuid.uuid4())[:8]  
        payment_slip = request.FILES["payment_slip"]
        
        Payment.objects.create(
            pid=payment_id,
            booking=booking,
            amount_paid=total_price,
            
            payment_status="Completed"
        )

        booking.status = "จองแล้ว"
        booking.save()

        messages.success(request, "✅ การชำระเงินสำเร็จ! ห้องของคุณถูกจองเรียบร้อยแล้ว")
        return redirect("booking_history") 

    context = {
        'booking': booking,
        'room': room,
        'nights': nights,
        'number': booking.number,
        'total_price': total_price,
    }
    return render(request, "payment.html", context)

def bookingDelete(request, id):
    booking = Booking.objects.get(bid = id)
    if request.method == 'POST':
        booking.delete()
        return redirect('manage_bookings')
    else:
        context = {'booking':booking}
        return render(request, 'Hotel/bookingDelete.html', context)
    
def usersDelete(request, id):
    customUser = CustomUser.objects.get(id = id)
    if request.method == 'POST':
        customUser.delete()
        return redirect('manage_users')
    else:
        context = {'customUser':customUser}
        return render(request, 'Hotel/usersDelete.html', context)


def booking_history(request):
    bookings = Booking.objects.filter(customer=request.user) 
    return render(request, 'booking_history.html', {'bookings': bookings})



from datetime import timedelta
from django.contrib.auth.models import *

from django.utils import timezone
from datetime import timedelta

from django.utils import timezone
from datetime import timedelta

def get_users():
    users = CustomUser.objects.all() 
    for user in users:
        user.is_online = user.last_login and timezone.now() - user.last_login < timedelta(minutes=5)
    return users

def manage_users(request):
    users = get_users()  
    return render(request, 'Hotel/manage_users.html', {'users': users})

 
def usersDetail(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'Hotel/usersDetail.html', {'user': user})













