คำแนะนำการติดตั้งและใช้งานโปรเจกต์ MiniproHotel จาก GitHub

1. ติดตั้งโปรเจกต์ โดยใช้คำสั่ง:
   git clone https://github.com/STIle-tech/MiniproHotel.git
   (แนะนำให้ clone ไว้ในโฟลเดอร์ชื่อ MiniproHotel)

2. สร้าง Virtual Environment และเปิดใช้งาน:
   python -m venv venv
   source venv/bin/activate  # สำหรับ macOS/Linux
   venv\Scripts\activate  # สำหรับ Windows

3. ติดตั้ง Package ต่าง ๆ ของโปรเจกต์:
   pip install -r requirements.txt

4. Log in เข้า MySQL โดยใช้ root:
   mysql -u root -p

5. สร้างฐานข้อมูลใน MySQL ชื่อ miniprohotel:
   CREATE DATABASE miniprohotel;

6. สร้าง User สำหรับฐานข้อมูล และกำหนดสิทธิ์:
   CREATE USER 'minipro68'@'localhost' IDENTIFIED BY '1234';
   GRANT ALL PRIVILEGES ON miniprohotel.* TO 'minipro68'@'localhost';
   FLUSH PRIVILEGES;

7. กำหนดค่าในไฟล์ settings.py ในส่วนของ DATABASES:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'miniprohotel',
           'USER': 'minipro68',
           'PASSWORD': '1234',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

8. รันคำสั่ง migrate เพื่อสร้างตารางข้อมูลใน MySQL:
   python manage.py migrate

9. สร้าง Superuser เพื่อใช้จัดการระบบ:
   python manage.py createsuperuser
   (ใส่ชื่อผู้ใช้, อีเมล และรหัสผ่านตามต้องการ)

10. รันเซิร์ฟเวอร์เพื่อทดสอบการทำงาน:
    python manage.py runserver

11. เข้าใช้งานระบบ
    - เปิดเบราว์เซอร์ไปที่ http://127.0.0.1:8000/admin/ และล็อกอินด้วยบัญชี Superuser ที่สร้างขึ้น

เพียงเท่านี้ก็สามารถติดตั้งและใช้งานโปรเจกต์ MiniproHotel ได้แล้ว 🎉
