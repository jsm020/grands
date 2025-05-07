
# Grands Django Project

Talabalar faoliyati va tashqi autentifikatsiya uchun Django REST API.

## Xususiyatlar
- Har bir faoliyat turi uchun alohida model (file upload, user, created_at)
- Fayl validatsiyasi: 30MB, .pdf, .doc, .docx, .png, .jpeg, .jpg
- Tashqi login API: foydalanuvchi login/parolni tashqi servisdа tekshiradi va tokenni saqlaydi
- Swagger UI: `/swagger/` orqali API hujjatlari va test

## Ishga tushirish
1. `.env` faylida `SAMDUKF_PERSONAL_TOKEN` ni belgilang
2. `pip install -r requirements.txt` (yoki kerakli paketlarni o‘rnating)
3. `python manage.py migrate`
4. `python manage.py runserver`

## Muhim endpointlar
- `/api/activities/login/` — tashqi login API
- `/admin/` — admin panel
- `/swagger/` — Swagger API hujjatlari

## Git ignore
`.env`, `__pycache__`, `*.pyc`, `staticfiles/`, `media/` va boshqa kesh fayllar gitga qo‘shilmaydi.
