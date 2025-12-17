from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            elif user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect")

    return render(request, 'LoginForm.html')


@login_required
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard_view.html')


@login_required
def user_dashboard_view(request):
    return render(request, 'user_dashboard_view.html')
