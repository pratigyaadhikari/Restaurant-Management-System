# Restaurant Management System

A RESTful Restaurant Management System built with **Django**, **Django REST Framework**, and **PostgreSQL**. The project provides APIs for managing restaurant operations, including food categories, menu items, table reservations, orders, payments, and user authentication.

## Features

- Token-Based Authentication
- Food Category & Menu Management
- Table Reservation System
- Order & Order Item Management
- Payment Integration (Khalti)
- Search, Filter & Ordering
- Pagination
- Swagger & ReDoc API Documentation

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- DRF Token Authentication
- drf-spectacular
- Khalti Payment API

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/pratigyaadhikari/Restaurant-Management-System.git
cd Restaurant-Management-System
```

2. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**Windows**

```bash
env\Scripts\activate
```

**macOS/Linux**

```bash
source env/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Run the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## API Documentation

- Swagger: `/api/schema/swagger-ui/`
- ReDoc: `/api/schema/redoc/`

## Project Structure

```text
Restaurant-Management-System/
├── category/
├── food/
├── order/
├── reservation/
├── payment/
├── restaurant/
├── images/
├── manage.py
├── requirements.txt
└── README.md
```

## Future Improvements

- JWT Authentication
- Email Notifications
- Online Table Booking
- Customer Reviews & Ratings
- Docker Support
- Unit Testing

## Author

**Pratigya Adhikari**

GitHub: https://github.com/pratigyaadhikari