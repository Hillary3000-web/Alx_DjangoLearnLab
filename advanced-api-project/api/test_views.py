from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Unit tests for the Book API endpoints including CRUD, 
    permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="Hillary Prince")
        self.book1 = Book.objects.create(title="Django Pro", publication_year=2023, author=self.author)
        self.book2 = Book.objects.create(title="API Mastery", publication_year=2025, author=self.author)
        
        # URL Endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # --- CRUD Tests ---

    def test_get_all_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book as an authenticated user."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "New Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating a book's title."""
        self.client.login(username='testuser', password='password123')
        update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {"title": "Updated Title", "publication_year": 2023, "author": self.author.id}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password123')
        delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Permissions Tests ---

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {"title": "Unauthorized", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Filtering, Searching, and Ordering Tests ---

    def test_filter_books_by_year(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url, {'publication_year': 2025})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "API Mastery")

    def test_search_books_by_title(self):
        """Test searching for a book by title."""
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Django Pro")

    def test_order_books_by_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.data[0]['title'], "Django Pro")