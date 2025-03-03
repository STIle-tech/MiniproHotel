คำแนะนำการติดตั้งและใช้งานโปรเจกต์ MiniproHotel จาก GitHub

1. ติดตั้งโปรเจกต์ โดยใช้คำสั่ง:
   git clone https://github.com/STIle-tech/MiniproHotel.git
   (แนะนำให้ clone ไว้ในโฟลเดอร์ชื่อ MiniproHotel)
   
 2.ใช้คำสั้ง ใน Terminal
   cd MiniproHotel

3. สร้าง Virtual Environment และเปิดใช้งาน:
   python -m venv venv
   
4. ติดตั้ง Package ต่าง ๆ ของโปรเจกต์:
   pip install -r requirements.txt

5. Log in เข้า MySQL โดยใช้ root:

6. สร้างฐานข้อมูลใน MySQL ชื่อ miniprohotel:
   CREATE DATABASE miniprohotel;

7. สร้าง User สำหรับฐานข้อมูล และกำหนดสิทธิ์:
   สร้าง user ชื่อ minipro68 พร้อมกำหนด รหัสผ่าน 1234 

8. รันคำสั่ง migrate เพื่อสร้างตารางข้อมูลใน MySQL:
   python manage.py migrate

9. สร้าง Superuser เพื่อใช้จัดการระบบ:
   python manage.py createsuperuser
   (ใส่ชื่อผู้ใช้, อีเมล และรหัสผ่านตามต้องการ)

10. รันเซิร์ฟเวอร์เพื่อทดสอบการทำงาน:
    python manage.py runserver



เพียงเท่านี้ก็สามารถติดตั้งและใช้งานโปรเจกต์ MiniproHotel ได้แล้ว 🎉
