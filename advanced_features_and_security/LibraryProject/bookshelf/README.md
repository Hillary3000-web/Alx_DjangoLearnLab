# Permissions and Groups Setup

## Custom Permissions
The Book model includes the following custom permissions:
- can_view: Allows a user to view the list of books.
- can_create: Allows a user to add a new book.
- can_edit: Allows a user to modify existing book details.
- can_delete: Allows a user to remove a book from the library.

## Groups Configuration
1. **Viewers**: Assigned the 'can_view' permission.
2. **Editors**: Assigned 'can_view', 'can_create', and 'can_edit' permissions.
3. **Admins**: Assigned all permissions (view, create, edit, delete).

## Usage
Permissions are enforced in 'views.py' using the '@permission_required' decorator.
