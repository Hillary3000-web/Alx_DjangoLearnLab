from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from  django.contrib.auth.views import LogoutView

# Login view using Django built-in LoginView
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using Django built-in LogoutView
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    http_method_names = ['get']

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
