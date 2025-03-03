from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.timezone import now
from django.contrib.auth.forms import UserChangeForm


       
class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('customer', 'ลูกค้า'),
        ('employee', 'พนักงาน'),
        ('admin', 'admin'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    position = forms.CharField(max_length=100, required=False) 
    birth_date = forms.DateField(required=False)  
    gender = forms.ChoiceField(choices=[('male', 'ชาย'), ('female', 'หญิง')], required=False)  

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role', 'phone', 'address', 'position', 'birth_date', 'gender']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        user.birth_date = self.cleaned_data.get('birth_date') 
        user.gender = self.cleaned_data.get('gender') 
        
        if commit:
            user.save()
            if user.role == 'customer':  
                CustomerProfile.objects.create(
                    user=user,
                    phone=self.cleaned_data.get('phone', ''),
                    address=self.cleaned_data.get('address', '')
                )
            elif user.role == 'employee':  
                EmployeeProfile.objects.create(
                    user=user,
                    phone=self.cleaned_data.get('phone', ''),
                    position=self.cleaned_data.get('position', '')
                )
        return user
    
class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('customer', 'ลูกค้า'),
        
        ('employee', 'พนักงาน'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'ชาย'),
        ('female', 'หญิง'),
        ('other', 'อื่นๆ'),
    ]

    username = forms.CharField(
        label="ชื่อผู้ใช้", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="อีเมล", 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    role = forms.ChoiceField(
        label="สิทธิ์การใช้งาน",
        choices=ROLE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label="เบอร์โทรศัพท์",
        max_length=15, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label="ที่อยู่",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), 
        required=False
    )
    birth_date = forms.DateField(
        label="วันเกิด",
        required=False, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    gender = forms.ChoiceField(
        label="เพศ",
        choices=GENDER_CHOICES, 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='male'
    )
    password1 = forms.CharField(
        label="รหัสผ่าน",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร และไม่เป็นรหัสผ่านที่เดาง่าย"
    )
    password2 = forms.CharField(
        label="ยืนยันรหัสผ่าน",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="กรอกรหัสผ่านอีกครั้งเพื่อยืนยัน"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'phone', 'address', 'birth_date', 'gender', 'password1', 'password2')
        labels = {
            'username': 'ชื่อผู้ใช้',
            'email': 'อีเมล',
            'role': 'สิทธิ์การใช้งาน',
            'phone': 'เบอร์โทรศัพท์',
            'address': 'ที่อยู่',
            'birth_date': 'วันเกิด',
            'gender': 'เพศ',
            'password1': 'รหัสผ่าน',
            'password2': 'ยืนยันรหัสผ่าน'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        user.birth_date = self.cleaned_data.get('birth_date', None)
        user.gender = self.cleaned_data.get('gender', None)

        if user.role == 'employee':
            user.is_staff = True
        elif user.role == 'admin':
            user.is_staff = True
            user.is_superuser = True

        if commit:
            user.save()
            if user.role == 'customer':
                CustomerProfile.objects.create(
                    user=user,
                    phone=self.cleaned_data.get('phone', ''),
                    address=self.cleaned_data.get('address', '')
                )
            elif user.role == 'employee':
                EmployeeProfile.objects.create(
                    user=user,
                    phone=self.cleaned_data.get('phone', ''),
                    position=self.cleaned_data.get('address', '')  
                )

        return user
    
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'roomname', 'category', 'price', 'address', 'roomsize', 'view', 'bed', 'image']
        
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'roomname': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.25'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'roomsize': forms.TextInput(attrs={'class': 'form-control'}),
            'view': forms.TextInput(attrs={'class': 'form-control'}),
            'bed': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

        labels = {
            'room_number': 'หมายเลขห้อง',
            'roomname': 'ชื่อห้อง',
            'category': 'ประเภทห้อง',
            'price': 'ราคา',
            'address': 'ที่อยู่',
            'roomsize': 'ขนาดห้อง (ตร.ม.)',
            'view': 'วิว',
            'bed': 'ประเภทเตียง',
            'image': 'อัปโหลดรูปภาพ',
        }

    def set_for_update(self):
        """ ใช้สำหรับอัปเดตห้อง ห้ามแก้ไขหมายเลขห้อง """
        self.fields['room_number'].widget.attrs['readonly'] = True
        self.fields['room_number'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['room_number'].label = 'หมายเลขห้อง (ไม่สามารถแก้ไข)'

class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="วันที่เช็คอิน"
    )
    check_out_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="วันที่เช็คเอาท์"
    )
    number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="จำนวนคนเข้าพัก"
    )

    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'number']
        labels = {
            'check_in_date': "วันที่เช็คอิน",
            'check_out_date': "วันที่เช็คเอาท์",
            'number': "จำนวนคนเข้าพัก",
        }
        widgets = {
            'room': forms.HiddenInput(), 
        }
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in_date")
        check_out = cleaned_data.get("check_out_date")
        today = now().date()

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError("❌ วันที่เช็คอินต้องน้อยกว่าวันที่เช็คเอาท์")
        
        if check_in and check_in < today:
            raise forms.ValidationError("❌ วันที่เช็คอินต้องเป็นวันที่ปัจจุบันหรืออนาคต")
        
        return cleaned_data


class PaymentForm(forms.ModelForm):
    payment_slip = forms.FileField(required=True, label="อัปโหลดสลิปการชำระเงิน")

    class Meta:
        model = Payment
        fields = ['payment_slip']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'ชื่อผู้ใช้',
            'email': 'อีเมล',
            'role': 'สิทธิ์การใช้งาน',
            'birth_date': 'วันเกิด',
            'gender': 'เพศ',
        }


class AddCatagoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['rid', 'name', 'description']
        widgets = {
            'rid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'rid': 'รหัสประเภทห้อง',
            'name': 'ชื่อประเภทห้อง',
            'description': 'รายละเอียด',
        }

    def set_for_update(self):
        """ ใช้สำหรับอัปเดตห้อง ห้ามแก้ไขหมายเลขห้อง """
        self.fields['rid'].widget.attrs['readonly'] = True
        self.fields['rid'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['rid'].label = 'รหัสประเภทห้อง (ไม่สามารถแก้ไข)'