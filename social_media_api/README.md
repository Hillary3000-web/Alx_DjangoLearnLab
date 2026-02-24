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

## Posts and Comments Endpoints
The API supports full CRUD operations for posts and comments, including pagination (10 items per page) and filtering.

* **Posts:** `GET /api/posts/` | `POST /api/posts/` | `GET /api/posts/<id>/` | `PUT /api/posts/<id>/` | `DELETE /api/posts/<id>/`
* **Comments:** `GET /api/comments/` | `POST /api/comments/` | `GET /api/comments/<id>/` | `PUT /api/comments/<id>/` | `DELETE /api/comments/<id>/`

### Filtering
You can search posts by title or content by appending `?search=<keyword>` to the URL.
Example: `GET /api/posts/?search=django`

### Permissions
* Any user can read (GET) posts and comments.
* You must be authenticated to create (POST) posts or comments.
* You must be the author of a post or comment to update (PUT) or delete (DELETE) it.

## Follows & Feed Features
Users can follow other users to curate a personalized feed of posts.

* **Follow User:** `POST /api/accounts/follow/<user_id>/` (Requires Authentication)
* **Unfollow User:** `POST /api/accounts/unfollow/<user_id>/` (Requires Authentication)
* **User Feed:** `GET /api/feed/` (Requires Authentication. Returns a paginated list of posts from followed users, ordered by most recent).

## Deployment Setup
This API is configured for production deployment using Gunicorn and WhiteNoise.

### Production Requirements
* `gunicorn`: Serves the application in production.
* `whitenoise`: Handles static file serving.
* `dj-database-url` & `psycopg2-binary`: For PostgreSQL database connection.

### Security Configurations
* `DEBUG = False`
* `SECURE_BROWSER_XSS_FILTER = True`
* `X_FRAME_OPTIONS = 'DENY'`
* `SECURE_CONTENT_TYPE_NOSNIFF = True`
* `SECURE_SSL_REDIRECT = True`

### Deployment Steps
1. Clone the repository to the production server.
2. Set environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`).
3. Install dependencies: `pip install -r requirements.txt`.
4. Run migrations: `python manage.py migrate`.
5. Collect static files: `python manage.py collectstatic`.
6. Start the server using Gunicorn: `gunicorn social_media_api.wsgi`.