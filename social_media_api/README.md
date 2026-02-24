# Social Media API

A backend RESTful API for a social media platform built with Django and Django REST Framework.

## Setup Instructions

1. Clone the repository and navigate to the directory: `cd Alx_DjangoLearnLab/social_media_api`
2. Install dependencies: `pip install django djangorestframework pillow`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## User Model
The API uses a Custom User model extending Django's `AbstractUser`. It includes extra fields for `bio`, `profile_picture`, and a `followers` ManyToMany relationship.

## Authentication Endpoints
Token-based authentication is used.
* **Register:** `POST /api/accounts/register/` (Requires: username, email, password. Returns: Token)
* **Login:** `POST /api/accounts/login/` (Requires: username, password. Returns: Token)
* **Profile:** `GET / PUT /api/accounts/profile/` (Requires Authentication Token in header: `Authorization: Token <your_token>`)