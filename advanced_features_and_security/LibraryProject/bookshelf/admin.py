from django.contrib import admin
from .models import Book

# Custom admin class
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filters in the sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')

# Register Book model with custom admin
admin.site.register(Book, BookAdmin)
