from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add_book/', views.add_book, name='add_book'),          # ✅ must be "add_book/"
    path('books/<int:pk>/edit_book/', views.edit_book, name='edit_book'),  # ✅ must be "edit_book/"
    path('books/<int:pk>/delete_book/', views.delete_book, name='delete_book'), # ✅ must be "delete_book/"
]


urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),
]

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

# Appending new views and patterns to the existing list
from .views import list_books, LibraryDetailView

urlpatterns += [
    path('list_books/', list_books, name='list_books'),
    path('library_detail/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
