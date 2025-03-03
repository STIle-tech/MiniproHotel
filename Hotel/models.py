from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'ลูกค้า'),
        ('employee', 'พนักงาน'),
        ('admin', 'admin'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'ชาย'),
        ('female', 'หญิง'),
        ('other', 'อื่นๆ'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone}"

class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class RoomCategory(models.Model):
    rid = models.CharField(max_length=13, primary_key=True, default='')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.rid} ({self.name})"
    

class Room(models.Model):
    roomname = models.CharField(max_length=50, default='')
    room_number = models.CharField(max_length=13, primary_key=True, default='') #แก้ชื่อให้ดูง่ายกว่านี้
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    address = models.CharField(max_length=200, default='')
    roomsize = models.CharField(max_length=50, default='')
    view = models.CharField(max_length=50, default='')
    bed =  models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='room/', null=True, blank=True)
    
    def __str__(self):
        return f"Room {self.room_number} - {self.category.name}"


class Booking(models.Model):
    bid = models.CharField(max_length=13, primary_key=True, editable=False)  # เอา default ออก
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    number = models.CharField(max_length=50, default='')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def save(self, *args, **kwargs):
        if not self.bid:  
            self.bid = uuid.uuid4().hex[:10]  
        if self.check_in_date and self.check_out_date:
            nights = (self.check_out_date - self.check_in_date).days
            self.total_price = nights * self.room.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.bid} - {self.customer.username} ({self.room.room_number})"


class Payment(models.Model):
    pid = models.CharField(max_length=13, primary_key=True, default=uuid.uuid4().hex[:10], editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ], default='Pending')

    def __str__(self):
        return f"Payment for {self.pid} - {self.amount_paid}"
