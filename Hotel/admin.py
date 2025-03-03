from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'birth_date', 'gender')}),  # เพิ่มฟิลด์ใหม่
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_role', 'get_birth_date', 'get_gender', 'phone', 'address')
    fields = ('user', 'phone', 'address', 'get_role', 'get_birth_date', 'get_gender')  # เพิ่มให้แสดงในหน้าแก้ไข
    readonly_fields = ('get_role', 'get_birth_date', 'get_gender')  # ป้องกันการแก้ไขค่า

    def get_role(self, obj):
        return obj.user.role
    get_role.short_description = 'Role'

    def get_birth_date(self, obj):
        return obj.user.birth_date
    get_birth_date.short_description = 'Birth Date'

    def get_gender(self, obj):
        return obj.user.gender
    get_gender.short_description = 'Gender'

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_role', 'get_birth_date', 'get_gender', 'phone', 'position')
    fields = ('user', 'phone', 'position', 'get_role', 'get_birth_date', 'get_gender')  # เพิ่มฟิลด์ในหน้าแก้ไข
    readonly_fields = ('get_role', 'get_birth_date', 'get_gender')  # ป้องกันการแก้ไขค่า

    def get_role(self, obj):
        return obj.user.role
    get_role.short_description = 'Role'

    def get_birth_date(self, obj):
        return obj.user.birth_date
    get_birth_date.short_description = 'Birth Date'

    def get_gender(self, obj):
        return obj.user.gender
    get_gender.short_description = 'Gender'