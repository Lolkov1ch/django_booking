# Booking (Django)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![Django](https://img.shields.io/badge/Django-4.x%2F5.x-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)  

---

## 📌 Опис
**Booking** – веб-додаток для бронювання кімнат, реалізований на Django.  
Користувачі можуть переглядати доступні кімнати, бронювати їх та відстежувати свої бронювання через особистий кабінет.  

---

## ⚙️ Функціонал
- Реєстрація та авторизація користувачів  
- Перегляд списку об’єктів (кімнат)  
- Пошук та фільтрація об’єктів  
- Деталі об’єкта з можливістю бронювання  
- Особистий кабінет користувача для перегляду бронювань  

---

## 📂 Структура проекту
```
booking/django_booking/booking_site/
├─ booking_app/ # Основний застосунок
├─ booking_site/ # Налаштування Django
├─ templates/ # HTML-шаблони
├─ static/ # CSS, JS, зображення
├─ db.sqlite3 # База даних
├─ manage.py
└─ requirements.txt # Залежності проект
```
---

## 🖼️ Скріншоти

| Головна сторінка | Вхід | Реєстрація | Деталі кімнати |
|-----------------|------|------------|----------------|
| ![Main](docs/screenshots/list.png) | ![Login](docs/screenshots/log.png) | ![Registration](docs/screenshots/reg.png) | ![Room Info](docs/screenshots/room_info.png) |

---

## 📦 Пакети (requirements)

Django==5.2.6
asgiref==3.9.1
django-widget-tweaks==1.5.0
sqlparse==0.5.3
tzdata==2025.2

---

## 🚀 Запуск проекту

```bash
# Клонувати репозиторій
git clone https://github.com/username/booking.git
cd booking

# Створити та активувати віртуальне середовище
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Встановити залежності
pip install -r requirements.txt

# Виконати міграції
python manage.py migrate

# Створити суперкористувача для адмінки
python manage.py createsuperuser

# Запустити сервер
python manage.py runserver

# Відкрити в браузері
http://127.0.0.1:8000/
