

# Student Activities Django REST API

Ushbu loyiha talabalarning faoliyatlarini boshqarish uchun yaratilgan Django REST API bo‘lib, quyidagi imkoniyatlarni taqdim etadi:

## Xususiyatlar

- **Faoliyatlar uchun fayl yuklash:** Har bir faoliyat turi uchun alohida model va fayl yuklash imkoniyati (max 30MB, ruxsat etilgan formatlar: pdf, doc, docx, png, jpeg, jpg).
- **Tashqi autentifikatsiya:** Foydalanuvchi login va parol orqali tashqi API (`https://student.samdukf.uz/rest/v1/auth/login`) orqali autentifikatsiyadan o‘tadi, token olinadi va saqlanadi.
- **Profil va GPA sinxronizatsiyasi:** Tashqi API orqali foydalanuvchi profili va GPA balli olinib, bazaga saqlanadi.
- **Foydalanuvchi cheklovi:** Faqat 1-kurs talabalari ro‘yxatdan o‘ta oladi, boshqalar rad etiladi.
- **JWT autentifikatsiya:** SimpleJWT orqali JWT access/refresh tokenlar generatsiya qilinadi (access token muddati 1 kun).
- **Admin/Superuser imkoniyatlari:** Admin/Superuser barcha yozuvlarni ko‘ra oladi va barcha fayl yuklash API-laridan foydalanishi mumkin.
- **Swagger va ReDoc:** API hujjatlari va fayl yuklash imkoniyati Swagger va ReDoc orqali ko‘rsatiladi.
- **.env va .gitignore:** Maxfiy ma’lumotlar va kesh fayllar .env va .gitignore orqali boshqariladi.

## O‘rnatish

1. **Klonlash va kutubxonalarni o‘rnatish:**
    ```bash
    git clone <repo-url>
    cd grands
    pip install -r requirements.txt
    ```

2. **.env faylini to‘ldiring:**
    ```
    SAMDUKF_PERSONAL_TOKEN=...
    SECRET_KEY=...
    ```

3. **Migratsiyalar va superuser yaratish:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4. **Serverni ishga tushiring:**
    ```bash
    python manage.py runserver
    ```

## API-lar

- **/api/activities/login/** – Tashqi API orqali login, JWT tokenlar qaytariladi.
- **/api/activities/[faoliyatlar]/** – Har bir faoliyat uchun fayl yuklash va CRUD (faqat o‘z yozuvlari, admin uchun hammasi).
- **/swagger/** va **/redoc/** – API hujjatlari va fayl yuklash imkoniyati.

## Muhim

- Faqat 1-kurs talabalari ro‘yxatdan o‘ta oladi.
- Fayl yuklash uchun JWT access token talab qilinadi.
- Admin/Superuser barcha yozuvlarni ko‘ra oladi va boshqaradi.

---

Agar maxsus o‘zgartirishlar yoki savollar bo‘lsa, so‘rashingiz mumkin!
