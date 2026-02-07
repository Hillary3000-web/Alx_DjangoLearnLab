# Advanced API Project - Django Learn Lab

## 1. Models and Serializers (Task 0)
This section covers the core data structure and how data is transformed for the API.

### Data Models
* **Author**: Stores the name of the author.
* **Book**: Stores the title and publication year, linked to an Author via a `ForeignKey`.
* **Relationship**: A one-to-many relationship exists from Author to Books, allowing one author to have multiple book entries.

### Custom Serializers
* **BookSerializer**: Manages the serialization of all book fields and includes a custom validator to ensure the `publication_year` is not in the future.
* **AuthorSerializer**: Serializes author information and dynamically nests the `BookSerializer` to provide a full list of books associated with that author.

---

## 2. API Views and Permissions (Task 1)
This section details the endpoints available and the security measures in place.

### View Configurations
The API utilizes Django REST Framework's generic views to provide full CRUD (Create, Read, Update, Delete) functionality:
* **BookListView**: `GET /api/books/` — Retrieves a list of all books.
* **BookDetailView**: `GET /api/books/<int:pk>/` — Retrieves a single book by its ID.
* **BookCreateView**: `POST /api/books/create/` — Allows creation of new books.
* **BookUpdateView**: `PUT/PATCH /api/books/update/<int:pk>/` — Allows updating existing books.
* **BookDeleteView**: `DELETE /api/books/delete/<int:pk>/` — Allows deletion of books.

### Permissions Setup
Access control is enforced using DRF's built-in permission classes:
* **IsAuthenticatedOrReadOnly**: Applied to list and detail views, allowing public read access while restricting write operations to logged-in users.
* **IsAuthenticated**: Applied to create, update, and delete views to ensure only registered users can modify the database.

---

## 3. Filtering, Searching, and Ordering (Task 2)
The `BookListView` supports advanced querying capabilities to improve data retrieval:

* **Filtering**: Users can filter books by `title`, `author`, and `publication_year`.
* **Searching**: Text-based search is enabled on the `title` and author's `name`.
* **Ordering**: Results can be sorted by `title` or `publication_year`.

### Usage Examples
| Feature | Query Parameter | Example URL |
| :--- | :--- | :--- |
| **Filter by Year** | `?publication_year=YYYY` | `/api/books/?publication_year=2025` |
| **Search** | `?search=term` | `/api/books/?search=Django` |
| **Ordering (Desc)** | `?ordering=-field` | `/api/books/?ordering=-publication_year` |

## 4. API Testing (Task 3)
A comprehensive test suite is located in `api/test_views.py` to ensure endpoint integrity.

### Testing Strategy
- **CRUD Operations**: Verified through `GET`, `POST`, `PUT`, and `DELETE` requests.
- **Permissions**: Confirmed that unauthenticated users are restricted from write operations.
- **Queries**: Tested filtering by year, searching by title, and ordering by publication date.

### How to Run Tests
Run the following command in the project root:
```bash
python manage.py test api